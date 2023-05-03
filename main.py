from app import app_server

if __name__ == '__main__':
    """
    #app.run(host='0.0.0.0', debug=True)
    #cert = './cert/cert.crt'
    #key = './cert/chave.key'
    #app.run(debug=False, ssl_context=(cert, key))
    """
    app_server.run(debug=False)
