# Deployment Instructions for christopherrehm.de

## Server Connection
- **Host:** 82.165.32.162
- **User:** claude
- **SSH Key:** ~/.ssh/id_ed25519

## Web Root
/var/www/christopherrehm.de/

## Upload Files
```bash
scp -i ~/.ssh/id_ed25519 [filename] claude@82.165.32.162:/var/www/christopherrehm.de/
```

## Upload Multiple Files
```bash
scp -i ~/.ssh/id_ed25519 file1.html file2.html file3.css claude@82.165.32.162:/var/www/christopherrehm.de/
```

## Verify Upload
```bash
ssh claude@82.165.32.162 "ls -la /var/www/christopherrehm.de/[filename]"
```

## Check File Content
```bash
ssh claude@82.165.32.162 "grep 'search_text' /var/www/christopherrehm.de/[filename]"
```

## Example: Deploy Portfolio Page
```bash
# Upload both modified index.html and new portfolio.html
scp -i ~/.ssh/id_ed25519 index.html portfolio.html claude@82.165.32.162:/var/www/christopherrehm.de/

# Verify
ssh claude@82.165.32.162 "ls -la /var/www/christopherrehm.de/portfolio.html"
ssh claude@82.165.32.162 "grep 'Portfolio' /var/www/christopherrehm.de/index.html"
```
