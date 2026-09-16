import tkinter as tk
from tkinter import ttk, messagebox
from urllib.parse import urlparse
import json, os, random

APP_NAME="Viral Post Optimizer Pro"

HOOKS=[
"Stop scrolling — the last part is worth seeing.",
"Most people miss this. Watch closely.",
"This is the part everyone is talking about.",
"Wait until the end before you judge it.",
"Here's what makes this post stand out."
]
CTA=["What do you think? Tell us below.","Would you do the same? Comment your take.","Tag someone who needs to see this.","Save this and come back to it later."]

def analyze():
    url=url_var.get().strip()
    platform=platform_var.get()
    topic=topic_var.get().strip()
    if not url or not url.startswith(("http://","https://")):
        messagebox.showerror(APP_NAME,"Please paste a valid public post/video URL.")
        return
    domain=urlparse(url).netloc.lower()
    detected=platform
    for name,key in [("TikTok","tiktok"),("Instagram","instagram"),("Facebook","facebook"),("YouTube","youtube"),("Pinterest","pinterest"),("X","x.com")]:
        if key in domain: detected=name; break
    hook=random.choice(HOOKS)
    cta=random.choice(CTA)
    caption=f"{hook}\n\n{topic or 'This post'}\n\n{cta}"
    hashtags={
      "TikTok":"#fyp #trending #viral #foryou #tiktok",
      "Instagram":"#reels #trending #viral #explore #contentcreator",
      "Facebook":"#trending #viral #facebookreels #mustwatch",
      "YouTube":"#shorts #trending #viral #youtube",
      "Pinterest":"#pinterest #ideas #trending #inspiration",
      "X":"#trending #viral #news"
    }.get(detected,"#viral #trending")
    out.delete("1.0",tk.END)
    out.insert(tk.END,f"PLATFORM: {detected}\n\nHOOK\n{hook}\n\nCAPTION\n{caption}\n\nHASHTAGS\n{hashtags}\n\nAUTO-APPLY STATUS\nReady for platform API connection.\n\nIMPORTANT\nThis app prepares and optimizes content. Actual publishing/editing requires the platform's official API and user authorization. It does not create fake engagement or guarantee viral reach.")

def copy_result():
    root.clipboard_clear(); root.clipboard_append(out.get("1.0",tk.END)); root.update()
    messagebox.showinfo(APP_NAME,"Optimized content copied.")

root=tk.Tk(); root.title(APP_NAME); root.geometry("900x700"); root.minsize(760,600)
style=ttk.Style(); style.configure("TButton",padding=8); style.configure("TLabel",font=("Segoe UI",11))
frame=ttk.Frame(root,padding=25); frame.pack(fill="both",expand=True)
ttk.Label(frame,text="🚀 Viral Post Optimizer Pro",font=("Segoe UI",22,"bold")).pack(anchor="w")
ttk.Label(frame,text="Analyze a public link, generate optimized content, and prepare it for official API publishing.",foreground="#555").pack(anchor="w",pady=(4,18))
ttk.Label(frame,text="Post / Video URL").pack(anchor="w")
url_var=tk.StringVar(); ttk.Entry(frame,textvariable=url_var).pack(fill="x",pady=(4,14))
row=ttk.Frame(frame); row.pack(fill="x")
platform_var=tk.StringVar(value="Auto Detect")
ttk.Label(row,text="Platform").pack(side="left")
ttk.Combobox(row,textvariable=platform_var,values=["Auto Detect","Facebook","Instagram","TikTok","YouTube","Pinterest","X"],state="readonly",width=18).pack(side="left",padx=10)
ttk.Label(row,text="Topic / description").pack(side="left",padx=(20,5))
topic_var=tk.StringVar(); ttk.Entry(row,textvariable=topic_var).pack(side="left",fill="x",expand=True)
btns=ttk.Frame(frame); btns.pack(fill="x",pady=18)
ttk.Button(btns,text="Analyze & Optimize",command=analyze).pack(side="left")
ttk.Button(btns,text="Copy Result",command=copy_result).pack(side="left",padx=10)
out=tk.Text(frame,font=("Consolas",11),wrap="word",height=25)
out.pack(fill="both",expand=True)
out.insert("1.0","Paste a public post/video link above, then click Analyze & Optimize.")
root.mainloop()
