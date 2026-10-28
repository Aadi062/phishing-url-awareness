import unittest

from phishing_checker import has_warnings, inspect_url


class PhishingCheckerTests(unittest.TestCase):
    def test_safe_url_has_no_warning_signs(self):
        findings = inspect_url("https://www.example.com/login")
        self.assertEqual(
            findings,
            ["No listed warning signs found. This does NOT prove safety."],
        )

    def test_http_and_ip_address_are_detected(self):
        findings = inspect_url("http://192.0.2.10/account")
        self.assertIn("Uses an IP address instead of a familiar domain.", findings)
        self.assertIn("Uses HTTP. HTTPS alone does not prove trust.", findings)
        self.assertTrue(has_warnings(findings))

    def test_at_symbol_and_http_are_detected(self):
        findings = inspect_url("http://example.com@sample.invalid/login")
        self.assertIn("Contains an @ symbol; inspect carefully.", findings)
        self.assertIn("Uses HTTP. HTTPS alone does not prove trust.", findings)

    def test_hostname_segments_are_detected(self):
        findings = inspect_url("https://a.b.c.d.e.example.invalid/path")
        self.assertIn("Contains many hostname segments/subdomains.", findings)

    def test_punycode_is_detected(self):
        findings = inspect_url("https://xn--example.invalid/")
        self.assertIn("Contains a punycode-style hostname.", findings)

    def test_malformed_url_does_not_crash(self):
        findings = inspect_url("http://[bad")
        self.assertEqual(findings, ["This text is not a valid URL format."])
        self.assertFalse(has_warnings(findings))

    def test_empty_input_is_handled(self):
        self.assertEqual(inspect_url(""), ["No URL entered."])


if __name__ == "__main__":
    unittest.main()
