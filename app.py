from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html>
<head>
<title>Yoga World</title>
<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: #f1f8f4;
  color: #333;
}
header {
  background: #2e7d5b;
  color: white;
  text-align: center;
  padding: 25px;
}
nav {
  background: #205b42;
  padding: 12px;
  text-align: center;
}
nav a {
  color: white;
  text-decoration: none;
  margin: 15px;
}
section {
  padding: 25px;
  margin: 20px;
  background: white;
  border-radius: 10px;
}
h2 {
  color: #2e7d5b;
}
footer {
  background: #2e7d5b;
  color: white;
  text-align: center;
  padding: 15px;
}
</style>
</head>

<body>

<header>
  <h1>Welcome to Yoga World</h1>
  <p>Discover Peace, Health and Balance</p>
</header>

<nav>
  <a href="#about">About</a>
  <a href="#benefits">Benefits</a>
  <a href="#types">Types</a>
  <a href="#poses">Yoga Poses</a>
</nav>

<section id="about">
  <h2>What is Yoga?</h2>
  <p>
    Yoga is an ancient practice that connects the body, mind and spirit.
    It includes physical postures, breathing exercises and meditation.
    Yoga helps people live a healthy and peaceful life.
  </p>
</section>

<section id="benefits">
  <h2>Benefits of Yoga</h2>
  <ul>
    <li>Improves flexibility and strength</li>
    <li>Reduces stress and anxiety</li>
    <li>Improves concentration</li>
    <li>Supports better sleep</li>
    <li>Helps maintain a healthy lifestyle</li>
  </ul>
</section>

<section id="types">
  <h2>Types of Yoga</h2>
  <ul>
    <li>Hatha Yoga – Basic physical postures and breathing</li>
    <li>Vinyasa Yoga – Flowing movements with breathing</li>
    <li>Ashtanga Yoga – Structured series of postures</li>
    <li>Kundalini Yoga – Breathing, meditation and movement</li>
  </ul>
</section>

<section id="poses">
  <h2>Basic Yoga Poses</h2>

  <h3>Mountain Pose (Tadasana)</h3>
  <p>A standing pose that helps improve posture and balance.</p>

  <h3>Tree Pose (Vrikshasana)</h3>
  <p>A balancing pose that improves focus and stability.</p>

  <h3>Cobra Pose (Bhujangasana)</h3>
  <p>A gentle backbend that stretches the front of the body.</p>

  <h3>Child's Pose (Balasana)</h3>
  <p>A relaxing pose used for rest and gentle stretching.</p>
</section>

<footer>
  <p>Yoga World | Healthy Body, Peaceful Mind</p>
</footer>

</body>
</html>
'''

@app.route('/health')
def health():
    return jsonify(status="ok")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)