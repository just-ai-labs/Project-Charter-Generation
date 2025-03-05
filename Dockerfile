# Use an official Node.js image as the base image
FROM node:18-alpine AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json first (for caching layers)
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the Next.js project
COPY . .

# Build the Next.js application
RUN npm run build

# Production Image
FROM node:18-alpine

# Set the working directory for the production environment
WORKDIR /app

# Copy only necessary files from the builder stage
COPY --from=builder /app/package.json /app/package-lock.json ./
COPY --from=builder /app/.next .next
COPY --from=builder /app/public public
COPY --from=builder /app/node_modules node_modules

# Set environment variables
ENV NODE_ENV=production
ENV PORT=3000

# Expose the port the app runs on
EXPOSE 3000

# Start the Next.js application
CMD ["npm", "start"]
