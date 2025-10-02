from flask import Flask, render_template, jsonify
import speedtest
import threading
import time

app = Flask(__name__)

# Global variable to store the latest speed test results
latest_results = {
    'download': 0,
    'upload': 0,
    'ping': 0,
    'timestamp': None,
    'testing': False
}

def run_speed_test():
    """Run speed test in background thread"""
    global latest_results
    
    try:
        latest_results['testing'] = True
        st = speedtest.Speedtest()
        
        # Get best server
        st.get_best_server()
        
        # Test download speed
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        latest_results['download'] = round(download_speed, 2)
        
        # Test upload speed
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        latest_results['upload'] = round(upload_speed, 2)
        
        # Get ping
        latest_results['ping'] = round(st.results.ping, 2)
        
        # Update timestamp
        latest_results['timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S')
        
    except Exception as e:
        print(f"Error during speed test: {e}")
        latest_results['download'] = 0
        latest_results['upload'] = 0
        latest_results['ping'] = 0
    
    finally:
        latest_results['testing'] = False

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/start-test')
def start_test():
    """Start speed test"""
    if not latest_results['testing']:
        thread = threading.Thread(target=run_speed_test)
        thread.daemon = True
        thread.start()
        return jsonify({'status': 'started'})
    else:
        return jsonify({'status': 'already_running'})

@app.route('/results')
def get_results():
    """Get current results"""
    return jsonify(latest_results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)