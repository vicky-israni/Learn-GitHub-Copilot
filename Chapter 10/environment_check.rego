package deployment

allow {
    input.environment == "prod"
} else {
    input.environment == "staging"
}