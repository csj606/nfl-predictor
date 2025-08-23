resource "aws_iam_role" "scheduler_trigger_role"{
    assume_role_policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Action = "sts:AssumeRole"
                Effect = "Allow"
                Sid = "AssumeSchedulerTriggerRole"
                Principal = {
                    Service = "scheduler.amazonaws.com"
                }
            }
        ]
    })
}

resource "aws_iam_policy" "trigger_season_week"{
    policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Action = ["lambda:InvokeFunction"]
                Effect = "Allow"
                Resource = var.season_week_arn
            }
        ]
    })
}

resource "aws_iam_role_policy_attachment" "season_week_connector"{
    role = aws_iam_role.scheduler_trigger_role.arn
    policy_arn = aws_iam_policy.trigger_season_week.arn
}

resource "aws_scheduler_schedule" "get_season_weeks" {
    flexible_time_window {
      mode = "OFF"
    }
    schedule_expression = "rate(365 days)"
    target {
        arn = var.season_week_arn
        role_arn = aws_iam_role.scheduler_trigger_role.arn
    }
}

resource "aws_iam_role" "weekly_update_triggerer" {
    assume_role_policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Action = "sts:AssumeRole"
                Effect = "Allowed"
                Sid = "AssumedWeeklyUpdateTriggererRole"
                Principal = {
                    Service = "scheduler.amazonaws.com"
                }
            }
        ]
    })
}

resource "aws_iam_policy" "allow_weekly_updator_call" {
    policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Action = ["lambda:InvokeFunction"]
                Effect = "Allowed"
                Resource = var.week_updator_arn
            }
        ]
    })
}

resource "aws_iam_role_policy_attachment" "week_update_connector"{
    role = aws_iam_role.weekly_update_triggerer.arn
    policy_arn = aws_iam_policy.allow_weekly_updator_call.arn
}

resource "aws_scheduler_schedule" "weekly_update" {
    flexible_time_window {
      mode = "OFF"
    }
    schedule_expression = "rate(7 days)"
    target {
      arn = var.week_updator_arn
      role_arn = aws_iam_role.weekly_update_triggerer.arn
    }
}

resource "aws_iam_role" "annual_stat_triggerer"{
    assume_role_policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Action = "sts:AssumeRole"
                Effect = "Allow"
                Sid = "AssumeAnnualStatsTriggerRole"
                Principal = {
                    Service = "scheduler.amazonaws.com"
                }
            }
        ]
    })
}

resource "aws_iam_policy" "allow_annual_stats_invoke"{
    policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Action = ["lambda:InvokeFunction"]
                Effect = "Allowed"
                Resource = var.annual_stats_arn
            }
        ]
    })
}

resource "aws_iam_role_policy_attachment" "annual_stats_connector" {
    role = aws_iam_role.annual_stat_triggerer.arn
    policy_arn = aws_iam_policy.allow_annual_stats_invoke.arn
}

resource "aws_scheduler_schedule" "get_annual_stats" {
    flexible_time_window {
      mode = "OFF"
    }
    target {
      arn = var.annual_stats_arn
      role_arn = aws_iam_role.annual_stat_triggerer.arn
    }
    schedule_expression = "rate(365 days)"
}