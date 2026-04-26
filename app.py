from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'mahalakshmi-secret-key'  # change in production

# Home / Welcome Page
@app.route('/')
def home():
    return render_template('welcome.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Dummy validation (replace with DB later)
        if username == "admin" and password == "1234":
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")

    return render_template('login.html')

# Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # For now just redirect (no DB)
        return redirect(url_for('login'))

    return render_template('signup.html')

# Dashboard (after login)
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', user=session['user'])
    return redirect(url_for('login'))

# Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
