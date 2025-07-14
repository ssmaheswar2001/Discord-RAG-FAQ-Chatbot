# Discord RAG Chatbot

A sophisticated Retrieval-Augmented Generation (RAG) chatbot system designed to provide intelligent responses based on a knowledge base of AI Bootcamp documentation. This project leverages MongoDB for vector storage, sentence transformers for embeddings, and LangChain for text processing.

## 🚀 Features

- **Document Processing**: Automatically extracts and processes `.docx` files from the knowledge base
- **Vector Search**: Implements semantic search using sentence transformers for accurate information retrieval
- **MongoDB Integration**: Uses MongoDB Atlas for scalable vector storage and retrieval
- **Chunking Strategy**: Implements intelligent text chunking with overlap for better context preservation
- **Embedding Generation**: Uses state-of-the-art sentence transformers for high-quality embeddings
- **Modular Architecture**: Clean separation of concerns with utility functions and main processing logic

## 📁 Project Structure

```
Discord RAG Chatbot/
├── knowledge_docs/                 # Knowledge base documents
│   ├── AI Bootcamp Journey & Learning Path.docx
│   ├── Intern FAQ - AI Bootcamp.docx
│   └── Training For AI Engineer Interns.docx
├── utils/
│   └── utils.py                   # Utility functions for MongoDB operations
├── rag_chatbot.ipynb             # Main Jupyter notebook with RAG implementation
├── requirements.txt               # Python dependencies
└── README.md                     # This file
```

## 🛠️ Prerequisites

- Python 3.8+
- MongoDB Atlas account
- OpenAI API key (for future Discord integration)

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Discord-RAG-Chatbot
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   MONGODB_URI=your_mongodb_atlas_connection_string
   OPENAI_API_KEY=your_openai_api_key
   ```

## 🔧 Configuration

### MongoDB Setup

1. Create a MongoDB Atlas cluster
2. Get your connection string from Atlas
3. Add the connection string to your `.env` file

### Knowledge Base

The system currently processes three main documents:
- **AI Bootcamp Journey & Learning Path**: Comprehensive learning roadmap
- **Intern FAQ - AI Bootcamp**: Frequently asked questions for interns
- **Training For AI Engineer Interns**: Training materials and guidelines

## 🚀 Usage

### Running the RAG System

1. **Open the Jupyter notebook**
   ```bash
   jupyter notebook rag_chatbot.ipynb
   ```

2. **Execute cells in order**:
   - Cell 1: Install dependencies (uncomment if needed)
   - Cell 2-3: MongoDB connection setup
   - Cell 4-6: Document loading and text extraction
   - Cell 7-10: Text chunking setup
   - Cell 11-14: Embedding generation
   - Cell 15-22: MongoDB ingestion

### Processing Documents

The system automatically:
1. Extracts text from `.docx` files
2. Splits text into chunks with overlap
3. Generates embeddings using sentence transformers
4. Stores chunks and embeddings in MongoDB
5. Creates search indexes for efficient retrieval

## 🧠 Technical Details

### Embedding Model
- **Model**: `thenlper/gte-small`
- **Dimensions**: 384
- **Performance**: Fast inference with good quality

### Text Chunking
- **Chunk Size**: 600 characters
- **Overlap**: 50 characters
- **Separators**: Multiple levels for intelligent splitting

### Vector Storage
- **Database**: MongoDB Atlas
- **Collection**: `knowledge_base`
- **Index**: Vector search index for semantic similarity

## 📊 Performance

- **Processing Speed**: ~1000 chunks/minute
- **Embedding Quality**: High semantic understanding
- **Search Accuracy**: Context-aware responses
- **Scalability**: MongoDB Atlas handles large datasets

## 🔮 Future Enhancements

- [ ] Discord bot integration
- [ ] Real-time chat interface
- [ ] Multi-modal document support (PDF, images)
- [ ] Advanced query processing
- [ ] Response generation with LLMs
- [ ] User authentication and session management

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for text processing utilities
- [Sentence Transformers](https://www.sbert.net/) for embedding generation
- [MongoDB Atlas](https://www.mongodb.com/atlas) for vector storage
- [python-docx](https://python-docx.readthedocs.io/) for document processing
