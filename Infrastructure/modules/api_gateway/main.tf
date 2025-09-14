resource "aws_apigatewayv2_api" "predict_api" {
    name = "nfl_predict_api"
    protocol_type = "HTTP"
}

resource "aws_apigatewayv2_integration" "get_games" {
    integration_type = "AWS_PROXY"
    api_id = aws_apigatewayv2_api.predict_api.id
    integration_uri = var.games_url
}

resource "aws_apigatewayv2_integration" "get_prediction" {
    api_id = aws_apigatewayv2_api.predict_api.id
    integration_type = "AWS_PROXY"
    integration_uri = var.predictor_url
}

resource "aws_apigatewayv2_route" "prediction_route" {
    api_id = aws_apigatewayv2_api.predict_api.id
    route_key = "GET /prediction"
    target = "integrations/${aws_apigatewayv2_integration.get_prediction.id}"
}

resource "aws_apigatewayv2_route" "game_route" {
    api_id = aws_apigatewayv2_integration.predict_api.id
    route_key = "GET /games"
    target = "integrations/${aws_apigatewayv2_integration.get_games.id}"
}

resource "aws_lambda_permission" "api_gateway_perm_prediction" {
    principal = "apigateway.amazonaws.com"
    function_name = "predictor"
    action = "lambda:InvokeFunction"
    source_arn = "${aws_apigatewayv2_api.predict_api.execution_arn}/*/*"
}

resource "aws_lambda_permission" "api_gateway_perm_games" {
    principal = "apigateway.amazonaws.com"
    function_name = "games"
    action = "lambda:InvokeFunction"
    source_arn = "${aws_apigatewayv2_api.predict_api.execution_arn}/*/*"
}