# 📡 WiFi Speed Test Web App# WiFi Tester Web App



A beautiful and modern web application to test your WiFi connection speed using Python Flask and the speedtest-cli library.A simple web application built with Python Flask to test WiFi connectivity and network performance.



![WiFi Speed Test](https://img.shields.io/badge/WiFi-Speed%20Test-blue?style=for-the-badge)## Features

![Python](https://img.shields.io/badge/Python-3.7+-green?style=for-the-badge&logo=python)

![Flask](https://img.shields.io/badge/Flask-2.3+-red?style=for-the-badge&logo=flask)🌐 **Internet Connectivity Test**

- Tests basic internet connection to Google

## ✨ Features- Shows response time and status



- 📊 **Real-time speed testing** using the same engine as speedtest.net📡 **Network Information**

- 💨 **Download speed** measurement (Mbps)- Displays hostname and local IP address

- ⬆️ **Upload speed** measurement (Mbps)- Shows WiFi interface details

- 🏓 **Ping latency** measurement (ms)

- 📱 **Responsive design** for mobile and desktop📡 **Ping Test**

- 🎨 **Modern glass-morphism UI** with beautiful gradients- Ping any host (default: Google DNS 8.8.8.8)

- ⏱️ **Timestamp** tracking of test results- Customizable ping count

- 🔄 **Real-time progress updates** during testing- Shows detailed ping results



## 🚀 Quick Start⚡ **Speed Test**

- Basic download speed test

### Prerequisites- Shows download time and speed in kbps

- Python 3.7 or higher

- pip (Python package installer)## Requirements



### Installation- Python 3.7+

- Flask

1. **Clone the repository:**- requests

   ```bash- psutil

   git clone https://github.com/yourusername/wifi-speedtest-app.git

   cd wifi-speedtest-app## Installation

   ```

1. Clone or download this project

2. **Create a virtual environment:**2. Navigate to the project directory:

   ```bash   ```bash

   python -m venv .venv   cd project01

   ```   ```



3. **Activate the virtual environment:**3. Create a virtual environment (recommended):

   - **Windows:**   ```bash

     ```bash   python -m venv .venv

     .venv\Scripts\activate   ```

     ```

   - **macOS/Linux:**4. Activate the virtual environment:

     ```bash   - Windows: `.venv\Scripts\activate`

     source .venv/bin/activate   - macOS/Linux: `source .venv/bin/activate`

     ```

5. Install required packages:

4. **Install dependencies:**   ```bash

   ```bash   pip install flask requests psutil

   pip install -r requirements.txt   ```

   ```

## Running the Application

## 🎯 Usage

1. Start the Flask server:

1. **Start the application:**   ```bash

   ```bash   python app.py

   python app.py   ```

   ```

2. Open your web browser and go to:

2. **Open your web browser** and navigate to:   ```

   ```   http://localhost:5000

   http://localhost:5000   ```

   ```

3. Use the web interface to test your WiFi connection!

3. **Click "Start Speed Test"** to begin testing your connection

## Project Structure

4. **Wait 30-60 seconds** for the test to complete and view your results!

```

## 🛠️ How It Worksproject01/

├── app.py              # Main Flask application

- **Backend:** Python Flask web framework provides the API endpoints├── templates/

- **Speed Testing:** Uses `speedtest-cli` library (same technology as speedtest.net)│   └── index.html      # Web interface template

- **Frontend:** Modern HTML5, CSS3, and JavaScript with real-time updates├── static/

- **Threading:** Background processing prevents UI blocking during tests│   └── style.css       # CSS styling

- **Real-time Updates:** AJAX polling shows progress and partial results└── README.md           # This file

```

## 📱 Design

## Features Details

The app features a beautiful glass-morphism design with:

- Gradient backgrounds### Internet Connectivity Test

- Transparent containers with backdrop blurTests connection to Google and measures response time.

- Smooth animations and transitions

- Mobile-responsive layout### Network Information

Retrieves and displays:

## 🌐 Network Access- Computer hostname

- Local IP address

The app runs on all network interfaces (`0.0.0.0`), making it accessible:- WiFi interface information

- **Locally:** `http://localhost:5000`

- **Network-wide:** `http://your-ip:5000` (accessible from other devices)### Ping Test

- Configurable host (default: 8.8.8.8)

## 📋 Technical Details- Configurable ping count (1-10)

- Cross-platform ping command execution

### File Structure

```### Speed Test

wifi-speedtest-app/- Downloads a small file from Google

├── app.py              # Main Flask application- Calculates download speed in kilobits per second

├── requirements.txt    # Python dependencies- Simple but effective for basic speed testing

├── templates/

│   └── index.html     # Web interface## Technical Notes

├── .gitignore         # Git ignore rules

└── README.md          # This file- Built with Flask web framework

```- Responsive design works on desktop and mobile

- Uses modern CSS with gradients and animations

### Dependencies- Cross-platform compatible (Windows, macOS, Linux)

- **Flask 2.3+** - Web framework- Error handling for network issues

- **speedtest-cli 2.1+** - Speed testing engine

## Security Note

### API Endpoints

- `GET /` - Main pageThis is a development server intended for local testing only. Do not use in production without proper security measures.

- `GET /start-test` - Start speed test

- `GET /results` - Get test results## License



## 🎨 Design FeaturesFree to use and modify for educational and personal projects.

- **Glass-morphism UI** with transparent backgrounds
- **Gradient colors** and smooth transitions
- **Responsive grid layout** for different screen sizes
- **Loading animations** and real-time feedback
- **Mobile-first design** that works on all devices

## 🔧 Configuration

The app runs with the following default settings:
- **Host:** `0.0.0.0` (all interfaces)
- **Port:** `5000`
- **Debug mode:** Enabled (disable for production)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Troubleshooting

### Common Issues:

**Speed test fails:**
- Check your internet connection
- Ensure firewall isn't blocking the app
- Try restarting the application

**Port already in use:**
- Change the port in `app.py` or stop other applications using port 5000

**Slow test results:**
- Speed tests can take 30-60 seconds - this is normal
- Results depend on your actual internet speed and server location

---

**Made with ❤️ using Python Flask**