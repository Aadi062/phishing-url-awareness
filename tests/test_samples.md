# Test Results

Python version used: 3.14.0 | Operating system: Windows 10 | Date: 2026-10-27

| # | Input | Expected result | Actual result | Pass/Fail |
|---|-------|-----------------|---------------|-----------|
| 1 | `https://www.example.com/login` | No listed warning signs | `No listed warning signs found. This does NOT prove safety.` | PASS |
| 2 | `http://192.0.2.10/account` | IP address + HTTP | `Uses an IP address instead of a familiar domain.`; `Uses HTTP. HTTPS alone does not prove trust.` | PASS |
| 3 | `http://example.com@sample.invalid/login` | @ symbol + HTTP | `Contains an @ symbol; inspect carefully.`; `Uses HTTP. HTTPS alone does not prove trust.` | PASS |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments | `Contains many hostname segments/subdomains.` | PASS |
| 5 | `https://xn--example.invalid/` | Punycode-style hostname | `Contains a punycode-style hostname.` | PASS |

## Notes

The five workbook samples produced the expected warnings. Testing the malformed
sample `http://[bad` also showed that the improvement safely returns a message
instead of crashing.

I also learned that HTTP is detected only when the supplied text is parsed as an
HTTP URL. No warning sign means caution is still needed rather than proof of safety.
