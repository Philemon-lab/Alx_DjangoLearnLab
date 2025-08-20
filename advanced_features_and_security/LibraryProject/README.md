#Adding Read me for Managing permissions and groups in Django

#HTTPS security Measures:
1. All HTTP requests are redirected to HTTPS using SECURE_SSL_REDIRECT.
2. HSTS is enforced with SECURE_HSTS_SECONDS, SECURE_HSTS_INCLUDE_SUBDOMAINS, and SECURE_HSTS_PRELOAD.
3. Session and CSRF cookies are transmitted only over HTTPS.
4. Security headers prevent clickjacking, content sniffing, and XSS attacks.
5. Ensure SSL/TLS certificates are installed and correctly configured on the server.