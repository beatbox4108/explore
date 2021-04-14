import markdown
class decorder:
    def __init__(self,text):
        "decord emd file"
        self.mdinstalse=markdown.Markdown(extensions=["abbr","attr_list","def_list","fanced_code","md_in_html","tables","code_hilits","toc","same_lists"])
        self.raw=text
        self.text=""
        self.meta={
            "ogp":{}
        }
        if text.split("\n")[0]=="$emd-format-meta":
            self.meta_avaliable=True
        for i in text.split("\n")[1:]:
            if i[0] and self.meta_avaliable:
                if i[:6]="$type=":
                    self.meta["type"]=i[6:]
                elif i[:7]="$title=":
                    self.meta["title"]=i[7:]
                elif i[:13]="$scriptsfile=":
                    self.meta["scriptfile"]=i[13:]
                elif i[:8]="$og-url=":
                    self.meta["ogp"]["url"]=i[8:]
                elif i[:9]="$og-type=":
                    self.meta["ogp"]["type"]=i[9:]
                elif i[:10]="$og-title=":
                    self.meta["ogp"]["title"]=i[10:]
                elif i[:16]="$og-description=":
                    self.meta["ogp"]["description"]=i[16:]
                elif i[:14]="$og-site_nane=":
                    self.meta["ogp"]["sitemane"]=i[14:]
                elif i[:9]="$og-image=":
                    self.meta["ogp"]["image"]=i[9:]
                else:self.meta_avaliable=False
            else:
                self.text+=i+"\n"
        self.html=self.mdinstalse.convert(self.text)