class hud:
	
	def open_settings():
		import tkinter as tk
		import config
		from tkinter import ttk
		from tkinter import Button
		from tkinter import Label
		from tkinter.messagebox import showinfo
		from get_info import info
		import time
		def region_changed(event):
			listget = info.get_district(current_var.get())
			combobox2['values'] = listget
			combobox2.set('')
		def switch():
			if current_var.get() != '':
				if current_var2.get() == '':
					var.set('Saved!')
					config.set('onlyregion', 'True')
					config.set('region', current_var.get())
					time.sleep(5)
					root.destroy()
				else:
					var.set('Saved!')
					config.set('onlyregion', 'False')
					config.set('region', current_var.get())
					config.set('district', current_var2.get())
					time.sleep(5)
					root.destroy()
		root = tk.Tk()
		root.geometry('300x200')
		root.resizable(False, False)
		root.title('AirRade Reworked')
		label = ttk.Label(text="Please select a region:")
		label.pack(fill=tk.X, padx=5, pady=5)
		current_var = tk.StringVar()
		combobox = ttk.Combobox(root, textvariable=current_var)
		combobox['values'] = info.get_region()
		combobox['state'] = 'readonly'
		combobox.pack(fill=tk.X, padx=5, pady=5)
		label2 = ttk.Label(text="Please select a district:")
		label2.pack(fill=tk.X, padx=5, pady=5)
		current_var2 = tk.StringVar()
		combobox2 = ttk.Combobox(root, textvariable= current_var2)
		combobox2['state'] = 'readonly'
		combobox2.pack(fill=tk.X, padx=5, pady=5)
		combobox.bind('<<ComboboxSelected>>', region_changed)
		b1 = Button(text="Save", command=switch)
		b1.pack(fill=tk.X, padx=5, pady=5)
		var = tk.StringVar()
		label = Label(root, textvariable = var)
		var.set(" ")
		label.pack()
		root.mainloop()		