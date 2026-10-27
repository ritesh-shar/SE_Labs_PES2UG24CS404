|Issues|Type | Line(s)	| Description |	Fix Approach |
|------| ----| -------- | ----------| ------- |
| 01 | Security (Bandit)| 11 | Hardcoding passwords directly in the source code exposes them to anyone with repository access.| Remove the raw string and fetch the secret dynamically via environment variables using os.getenv()|
|02| Security (Bandit) |	16 |	The md5 hashing algorithm is cryptographically weak and vulnerable to collision attacks.|	Replace hashlib.md5() with the more secure hashlib.sha256().|
|03| Security (Bandit) \ 56	 | Using os.system() with concatenated variables allows shell injection attacks if labPc contains malicious shell commands. |	Replace with subprocess.run() and pass arguments as a safe, shell-escaped list instead of a concatenated string. | 
|04| Bug/Quality (Pylint)	| 23 |	Passing a mutable object ({}) as a default argument in gradeStudent means the same dictionary instance is shared across all function calls.| 	Change default to None, then instantiate a new dictionary if penalties is None inside the function block. |
|05| Security (Bandit) |	20	random is a pseudo-random generator, which is predictable and unsuitable for security/exam purposes. |	Replace random.choice() with secrets.choice(), which uses an OS-level cryptographically secure random number generator. |
|06| Style (Pylint) | 25 | Iterating using range(len(QUESTIONS)) is an anti-pattern in Python and reduces readability. | Refactor the loop to use enumerate(QUESTIONS), which natively provides both the index and the item. |
