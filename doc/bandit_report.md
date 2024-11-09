### **`bandit_report.md`**

```
[main]    INFO    profile include tests: None
[main]    INFO    profile exclude tests: None
[main]    INFO    cli include tests: None
[main]    INFO    cli exclude tests: None
[main]    INFO    running on Python 3.11.2
Run started:    2024-11-09 22:32:05.472728

Files in scope (1):
        ./Desktop/example.py (score: {SEVERITY: 5, CONFIDENCE: 3})

Files excluded (0):

Test results:                                                                
>> Issue: [B608: hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.                                         
   Severity: Medium   Confidence: Low                                      
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)              
   More Info: https://bandit.readthedocs.io/en/1.7.10/plugins/b608_hardcoded_sql_expressions.html                                                         

   Location: ./Desktop/example.py:7:12
   Code:
   6           
   7           query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
   8           cursor.execute(query)

--------------------------------------------------

Code scanned:                                                                
        Total lines of code: 9
        Total lines skipped (#nosec): 0

Run metrics:                                                                 
        Total issues (by severity):
                Undefined: 0
                Low: 0
                Medium: 1
                High: 0
        Total issues (by confidence):
                Undefined: 0
                Low: 1
                Medium: 0
                High: 0

Files skipped (0):
```

---

### Breakdown of the Report:

1. **Detected Issue**: 
   - **B608** - This indicates a potential SQL injection vulnerability, as the SQL query is constructed using string concatenation without proper sanitization. This could allow an attacker to inject malicious SQL code.
   - **Severity**: Medium
   - **Confidence**: Low
   - **CWE**: [CWE-89: SQL Injection](https://cwe.mitre.org/data/definitions/89.html)
   - **Location**: The issue is located in `./Desktop/example.py` at line 7.

2. **Code**:
   - Line 7 contains the vulnerable code where user input (`username` and `password`) is directly inserted into the SQL query string.

3. **Run Metrics**: 
   - **Total Issues by Severity**: 1 medium severity issue.
   - **Total Issues by Confidence**: 1 low confidence issue.

---

### Recommendation for Fix:
To avoid SQL injection, it's important to use **parameterized queries** instead of string-based query construction. Here's how to fix it:

#### Vulnerable Code:
```python
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cursor.execute(query)
```

#### Fixed Code:
```python
query = "SELECT * FROM users WHERE username = %s AND password = %s"
cursor.execute(query, (username, password))
```

In this fix, the query is parameterized, and the user input is safely handled, preventing SQL injection.

