# 🚀 Quick Start - GitHub Pages Deployment

## 📁 Current Files
```
✅ index.html              # Main interactive graph (required)
✅ graph_gpt.dot           # Source data in DOT format (required)
✅ README.md               # Documentation
✅ create_github_pages.py  # Regeneration script
✅ .gitignore              # Git ignore rules
```

## 🌐 Deploy to GitHub Pages

### Step 1: Push to GitHub

```bash
# Initialize git (if not already done)
git init

# Add files
git add .

# Commit
git commit -m "Add interactive clinical graph"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git

# Push
git push -u origin main
```

### Step 2: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top right)
3. Scroll to **Pages** section (left sidebar)
4. Under **Source**:
   - Branch: Select **main**
   - Folder: Select **/ (root)**
5. Click **Save**
6. Wait 2-5 minutes

### Step 3: Access Your Graph

Your graph will be available at:
```
https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/
```

## 🔄 Update the Graph

If you need to modify descriptions or the graph structure:

1. Edit `create_github_pages.py` (change node descriptions)
   OR edit `graph_gpt.dot` (change structure)

2. Regenerate index.html:
```bash
python create_github_pages.py
```

3. Commit and push:
```bash
git add index.html
git commit -m "Update graph"
git push
```

4. Changes will appear on GitHub Pages in 1-2 minutes

## 📋 Files Explanation

| File | Purpose | Required for Pages? |
|------|---------|-------------------|
| `index.html` | Main interactive visualization | ✅ Yes |
| `graph_gpt.dot` | Source data | ✅ Yes (for regeneration) |
| `README.md` | Documentation | ⚠️ Recommended |
| `create_github_pages.py` | Regeneration script | ❌ No (development only) |
| `.gitignore` | Git ignore rules | ⚠️ Recommended |

## 🎨 Customization Tips

### Change Graph Title
Edit `create_github_pages.py`, line with:
```python
<h1>📊 Interactive Clinical Relations Graph</h1>
```

### Change Node Descriptions
Edit `create_github_pages.py`, in the `node_descriptions` dictionary:
```python
node_descriptions = {
    'mitotic_rate': '<b>Your Title</b><br><br>Your description here.',
    # ...
}
```

### Change Colors
Edit the `custom_header` section in `create_github_pages.py`:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

## 🐛 Troubleshooting

### Page shows 404
- Make sure you pushed `index.html` to the `main` branch
- Wait 5 minutes after enabling Pages
- Check Settings → Pages to see deployment status

### Graph doesn't load
- Open browser console (F12) to check for errors
- Make sure `index.html` is in the root directory
- Try clearing browser cache (Ctrl+Shift+R)

### Want to use a custom domain?
1. Go to Settings → Pages
2. Enter your domain in "Custom domain"
3. Follow GitHub's DNS configuration instructions

## 📚 Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [PyVis Documentation](https://pyvis.readthedocs.io/)
- [DOT Language Guide](https://graphviz.org/doc/info/lang.html)

## ✅ Checklist

- [ ] Files pushed to GitHub
- [ ] GitHub Pages enabled in Settings
- [ ] Waited 5 minutes for deployment
- [ ] Tested the live URL
- [ ] Updated README.md with correct URLs

---

**Your graph is ready! Share the link with colleagues!** 🎉
