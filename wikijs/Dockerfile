# Use the existing image as the base
FROM requarks/wiki:2

# Set environment variables
ENV DB_TYPE=sqlite

# Expose the port the application runs on
EXPOSE 3000

# Define the volume mount point
VOLUME ["/var/wiki/data"]

# Create the directory and set permissions (if needed)
USER root
RUN mkdir -p /var/wiki/data && chown -R node:node /var/wiki/data

# Switch to non-root user if required by the base image
USER node

# Define the default command
CMD ["node", "server"]

