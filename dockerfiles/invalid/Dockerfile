# Passes: Uses specific version tag
FROM alpine:3.19

# Passes: Sets non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Passes: Uses COPY instead of ADD
COPY ./local-file.txt /app/

RUN apk add --no-cache curl

CMD ["sh"]