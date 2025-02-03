# 📚 Write a book 🤖


**🏗️ Work in Progress 🏗️**

Generate Characters and relationship graph (stored in Neo4j), write each chapter (stored in Pinecone).

## Tech Stack

- LangChain
- OpenAI
- Pinecone
- Neo4j
- FastAPI
- React (Vite)


## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/avidness/novel-ai.git
   ```

1. Navigate to the project directory:
   ```bash
   cd novel-ai
   ```

1. Create an `.env` in the `/api` directory:
   ```bash
   OPENAI_API_KEY=<YOUR_KEY>
   PINECONE_API_KEY=<YOUR_KEY>
   ```

1. Start the services using Docker Compose:
   ```bash
   docker-compose up
   ```

## License
MIT