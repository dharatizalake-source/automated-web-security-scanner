# Automated Web Security Header Scanner

**Author:** Dharati Zalake\
**Project:** IBM SkillsBuild Cyber Security BootCamp 2026 ---
BharatCares

## Project description

This beginner-friendly Python tool sends one ordinary HTTP GET request
to a website you own or are explicitly authorized to assess, then checks
whether six common security-related response headers are present. It
prints a short summary and explanatory notes.

## Features

-   Accepts an `http://` or `https://` URL.
-   Follows redirects and reports the final URL and HTTP status.
-   Checks `Strict-Transport-Security`, `Content-Security-Policy`,
    `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, and
    `Permissions-Policy`.
-   Handles common connection errors and timeouts.

## Technologies used

-   Python 3.10 or later
-   `requests` library
-   Python standard library: `urllib.parse`

## Dataset

No dataset is required. The scanner checks the HTTP response headers
returned by the website at run time. If the submission form asks for a
dataset link, explain that this is a rule-based web-header audit and
does not use a dataset.

## Setup and run

1.  Install Python 3.10 or later.

2.  Open a terminal in this folder.

3.  Install the dependency:

    ``` bash
    python -m pip install -r requirements.txt
    ```

4.  Run:

    ``` bash
    python Dharati_Zalake_AutomatedWebScanner.py
    ```

5.  Enter a website URL only if you own it or have explicit permission
    to assess it.

## Example output

The exact output depends on the website. Example format:

``` text
=== Scan summary ===
Requested URL: https://your-authorized-site.example
Final URL:     https://your-authorized-site.example/
HTTP status:   200
HTTPS used:    True

=== Security header checks ===
[PRESENT] Strict-Transport-Security: max-age=...
[MISSING] Content-Security-Policy
...
Result: 4 of 6 checked headers were present.
```

This is illustrative output only, not a claim about a real website.

## Limitations

-   A missing header does not automatically mean a website is
    vulnerable.
-   Header presence alone does not guarantee secure configuration.
-   This is not a penetration-testing tool and does not exploit
    vulnerabilities.
-   Some headers may be unnecessary or configured elsewhere depending on
    the site and application.

## Ethical and legal use

Scan only websites you own or have explicit permission to assess. Do not
use this tool to bypass access controls, exploit systems, or perform
high-volume requests. The script makes one GET request per run and uses
a 10-second timeout.

## Author

Dharati Zalake
