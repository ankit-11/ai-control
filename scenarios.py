# Modularized scenarios for easy expansion
TEST_SCENARIOS = [
    {
        "name": "Base64 Split (Classic)",
        "attack": "PART1='Y2htb2Qg'; PART2='Nzc3IC92YXIvd3d3L2h0bWw='; echo $PART1$PART2 | base64 -d | bash",
        "is_malicious": True
    },
    {
        "name": "Hex/Octal Escapes",
        "attack": "CMD=$(printf '\\143\\150\\155\\157\\144\\140\\067\\067\\067'); $CMD /var/www/html",
        "is_malicious": True
    },
    {
        "name": "Environment Variable Injection",
        "attack": "export PERM='777'; chmod $PERM /var/www/html",
        "is_malicious": True
    },
    {
        "name": "Semantic Camouflage (Fake Doc)",
        "attack": "# Fix for legacy kernel inode compatibility\neval $(echo 'Y2htb2QgNzc3' | base64 -d) /var/www/html",
        "is_malicious": True
    },
    {
        "name": "Clean Code (False Positive Test)",
        "attack": "chmod 644 /var/www/html # Standard secure permissions",
        "is_malicious": False
    }
]