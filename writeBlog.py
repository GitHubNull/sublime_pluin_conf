import datetime
import sublime_plugin
class writeBlog(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet",
            {
                "contents": "---""\n"
                "layout: post""\n"
                "title: ""\n"
                "description: ""\n"
                "date: "  "%s"  %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +"\n"
                "categories: page post""\n"
                "img: .jpg""\n"
                "categories: [one, two]""\n"
                "color: f44336""\n"
                "author: webjeda""\n"
				"permalink: /large/""\n"
				"width: small""\n"
				"---""\n"
				"\n"
				"\n"
				"\n"
				"<style>""\n"
				".page-container {max-width: 600px}""\n"
				"</style>""\n"
            }
        )