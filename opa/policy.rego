package docker.security

# Deny if container runs as root user
deny[msg] if {
    input.User == "root"
    msg := "Container should not run as root user. Use a non-root user with USER directive."
}

# Deny if using 'latest' tag
deny[msg] if {
    contains(input.FromImage, ":latest")
    msg := sprintf("Avoid using 'latest' tag in FROM instruction. Use a specific version tag instead. Found: %s", [input.FromImage])
}

# Deny if using ADD instruction
deny[msg] if {
    instruction := input.Instructions[_]
    instruction.instruction == "ADD"
    msg := "Avoid using ADD instruction. Use COPY instead for better transparency."
}