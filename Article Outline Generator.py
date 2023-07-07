import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import openai
import threading


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Article Outline Generator')

        self.headings_frame = ttk.LabelFrame(self, text='Headings')
        self.headings_frame.pack(pady=10)
        
        self.headings_frame = ttk.LabelFrame(self, text='Headings')
        self.headings_frame.pack(pady=10)

        self.h2_var = tk.StringVar(value="2")
        self.h3_var = tk.StringVar(value="2")
        self.h4_var = tk.StringVar(value="0")

        ttk.Label(self.headings_frame, text='h2 headings').grid(column=0, row=0)
        ttk.Label(self.headings_frame, text='h3 headings').grid(column=1, row=0)
        ttk.Label(self.headings_frame, text='h4 headings').grid(column=2, row=0)

        ttk.Spinbox(self.headings_frame, from_=0, to=10, textvariable=self.h2_var).grid(column=0, row=1)
        ttk.Spinbox(self.headings_frame, from_=0, to=10, textvariable=self.h3_var).grid(column=1, row=1)
        ttk.Spinbox(self.headings_frame, from_=0, to=10, textvariable=self.h4_var).grid(column=2, row=1)

        # Row 2
        self.options_frame = ttk.LabelFrame(self, text='Options')
        self.options_frame.pack(pady=10)

        self.tone_var = tk.StringVar(value="Formal")
        self.style_var = tk.StringVar(value="Informative")
        self.lang_var = tk.StringVar(value="English")

        tone_options = ['Formal', 'Casual', 'Journalistic', 'Informative', 'Professional']
        style_options = ['Academic', 'Conversational', 'Informative', 'Narrative', 'Technical']
        lang_options = ['English', 'Dutch', 'Spanish ', 'French ', 'German']

        ttk.Label(self.options_frame, text='voice tone').grid(column=0, row=0)
        ttk.Label(self.options_frame, text='writing style').grid(column=1, row=0)
        ttk.Label(self.options_frame, text='language').grid(column=2, row=0)

        ttk.Combobox(self.options_frame, textvariable=self.tone_var, values=tone_options).grid(column=0, row=1)
        ttk.Combobox(self.options_frame, textvariable=self.style_var, values=style_options).grid(column=1, row=1)
        ttk.Combobox(self.options_frame, textvariable=self.lang_var, values=lang_options).grid(column=2, row=1)

        self.title_frame = ttk.LabelFrame(self, text='Blog post title')
        self.title_frame.pack(pady=10)

        self.title_entry = tk.Text(self.title_frame, height=2)
        self.title_entry.pack()

        self.prompt_frame = ttk.LabelFrame(self, text='Custom Prompts')
        self.prompt_frame.pack(pady=10)

        self.prompt_entry = tk.Text(self.prompt_frame, height=10)
        self.prompt_entry.pack()

        self.output_frame = ttk.LabelFrame(self, text='Post outline')
        self.output_frame.pack(pady=10)

        self.output_text = tk.Text(self.output_frame, height=10)
        self.output_text.pack()

        self.generate_btn = ttk.Button(self, text='Generate', command=self.generate)
        self.generate_btn.pack(pady=10)

        self.save_btn = ttk.Button(self, text='Save', command=self.save)
        self.save_btn.pack(pady=10)

    def generate(self):
        # Call function in a new thread
        threading.Thread(target=self._generate).start()

    def _generate(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        # Get the input values
      
        h2_value = self.h2_var.get()
        h3_value = self.h3_var.get()
        h4_value = self.h4_var.get()

        tone_value = self.tone_var.get()
        style_value = self.style_var.get()
        lang_value = self.lang_var.get()

        title_value = self.title_entry.get(1.0, tk.END).strip()
        prompt_value = self.prompt_entry.get(1.0, tk.END).strip()

        prompt = "You need to create blog post outline for a artcle. The title of the article is "+title_value+". You need to add "+h2_value+" number of "\
        "h2 headings and "+h3_value+" number of h3 headings and "+h4_value+" number of h4 headings into the outline. h3 headings must be inside the"\
        " h4 headings must be in appropriate h3 headings. You have a "+style_value+" writing style and "+tone_value+" tone of voice. You must mention"\
        " key points as list for each headings or sub headings. You MUST write outline in Markdown fomrmat"
        # print(prompt)

        if prompt_value:
            prompt = prompt_value

        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [{"role": "user", "content": prompt}]
        )

        answer = response.choices[0].message.content

        output_string =answer
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, output_string)

        print(answer)

        # Print the input values
        # print("h2 headings:", h2_value)
        # print("h3 headings:", h3_value)
        # print("h4 headings:", h4_value)
        # print("voice tone:", tone_value)
        # print("writing style:", style_value)
        # print("language:", lang_value)
        # print("Blog post title:", title_value)
        # print("Custom Prompts:", prompt_value)
        pass

    def save(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None: 
            return
        text2save = str(self.output_text.get(1.0, "end")) 
        f.write(text2save)
        f.close() # 'forget' this 

if __name__ == "__main__":
    app = Application()
    app.mainloop()
