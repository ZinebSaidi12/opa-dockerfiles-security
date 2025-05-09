# Violation 1: Uses 'latest'
FROM alpine:latest

# Violation 2: Runs as root (default or explicitly)
USER root

# Violation 3: Uses ADD
ADD https://example.com/file.tar.gz /tmp/

RUN apk add --no-cache curl
CMD ["sh"]
