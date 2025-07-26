resource "aws_glacier_vault" "backup" {
    name = "DatabaseBackup"
    tags = {
        name = "nfl"
    }
}