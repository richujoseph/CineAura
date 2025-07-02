# 🎬 **CineAura** – Your Smart Movie Recommendation Bot

An intelligent chatbot that helps users discover the perfect movie to watch based on their mood, preferences, or genre — powered by **Groq API** and a sleek Flask web app.

![CineAura Banner](https://github.com/richujoseph/CineAura/blob/main/chatbot/CeniAura.png?raw=true)


## 🌟 Features

* 🎞️ **Smart Movie Suggestions** by mood, genre, or personal taste
* 🤖 Built using **Groq's LLaMA model API** for intelligent responses
* 🌐 Interactive chatbot interface built with **Flask**
* 🔐 Secure API key management using `.env` and `python-dotenv`
* 💬 Seamless real-time chat experience with AJAX
* 🎨 **Stunning cinematic UI** with glassmorphism effects and animations
* 📱 **Fully responsive design** that works on all devices
* ✨ **Premium visual effects** including floating particles and gradient animations

## 📸 Preview

*Experience the magic of CineAura's premium interface:*

- **Cinematic dark theme** with space-inspired gradients
- **Professional chat bubbles** with smooth animations
- **Smart text formatting** for movie titles and recommendations
- **Typing indicators** and real-time message delivery
- **Glassmorphism effects** with backdrop blur

## 🚀 Getting Started

### 🔧 Requirements

* Python 3.9+
* pip package manager
* GitHub account
* Groq API Key (free from [groq.com](https://groq.com))

### 📥 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/richujoseph/CineAura.git
   cd CineAura
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` file in the root directory**
   ```env
   GROQ_API_KEY=your-groq-api-key-here
   ```
   
   > 💡 **Get Your API Key:** Visit [groq.com](https://groq.com), sign up for free, and generate your API key

5. **Run the application**
   ```bash
   python chatbot/app.py
   ```

6. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:5000
   ```
## 🧠 Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python 3.9+, Flask |
| **Frontend** | HTML5, CSS3, JavaScript (ES6+) |
| **AI Model** | LLaMA via Groq API |
| **Styling** | Custom CSS with Glassmorphism & Animations |
| **Architecture** | RESTful API with AJAX communication |

## 🎯 Usage Examples

**Ask CineAura:**
- *"Recommend me a horror movie for tonight"*
- *"I'm feeling sad, what should I watch?"*
- *"Best sci-fi movies from the 2010s"*
- *"Movies like Inception"*
- *"What's a good family movie for the weekend?"*

## 💡 Future Enhancements

* 🎵 **Music & Podcast Recommendations**
* 📽️ **IMDb Integration** with ratings and trailers
* 💾 **Favorites System** to save preferred movies
* 🔍 **Advanced Filtering** by year, rating, duration
* 👥 **User Profiles** with personalized recommendations
* 🎬 **Streaming Platform Integration**
* 📊 **Analytics Dashboard** for usage insights




## 🐛 Troubleshooting

### Common Issues:

**Issue**: `ModuleNotFoundError: No module named 'groq'`
**Solution**: Make sure you've activated your virtual environment and run `pip install -r requirements.txt`

**Issue**: `Invalid API Key`
**Solution**: Double-check your `.env` file and ensure your Groq API key is correct

**Issue**: `Port already in use`
**Solution**: Change the port in `app.py` or kill the process using the port

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙋‍♂️ Author

**Richu Joseph**
- 🔗 [GitHub Profile](https://github.com/richujoseph)
- 💼 [LinkedIn](https://linkedin.com/in/richujoseph)

## 🌟 Show Your Support

If you found this project helpful, please consider:
- ⭐ **Starring** this repository
- 🍴 **Forking** it for your own use
- 📢 **Sharing** it with others
- 🐛 **Reporting** any issues you find

---

<div align="center">
  <strong>🎬 Made with ❤️ for movie lovers everywhere 🎬</strong>
  <br>
  <sub>Discover your next favorite film with CineAura!</sub>
</div>
