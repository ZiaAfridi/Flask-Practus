from website import create_app

# Entry point to the app.
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    