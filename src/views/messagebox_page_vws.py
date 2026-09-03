import customtkinter as ctk


messagebox = None

def show_message_box(frame, title, text_, esqc_senha = False):

    global messagebox

    if messagebox is not None and messagebox.winfo_exists():
        return

    messagebox = ctk.CTkToplevel(frame,
        width = 325,
        height = 150
    )

    messagebox.title(title)
    messagebox.resizable(False, False)

    window_width = 325
    window_height = 150
    
    screen_width = messagebox.winfo_screenwidth()
    screen_height = messagebox.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height -  window_height) // 2

    messagebox.geometry(f'{window_width}x{window_height}+{x}+{y}')

    messagebox.transient(frame)
    messagebox.lift()

    if esqc_senha == False:

        label_text = ctk.CTkLabel(messagebox,
            width = 0,
            height = 0,
            text = text_,
            font = ('Inter', 18, 'bold'),
            wraplength = 320
        )

        label_text.pack(fill = 'both', expand = True, pady = (20, 0))
        messagebox.pack_propagate(False)

        def button_click():

            messagebox.destroy()

        button_ok = ctk.CTkButton(messagebox,
            width = 100,
            height = 25,
            text = 'Ok',
            cursor = 'hand2',
            font = ('Inter', 14, 'bold'),
            text_color = 'white',
            fg_color = '#5d3452',
            hover_color = '#754363',
            corner_radius = 5,
            command = button_click
        )

        button_ok.pack(pady = 25)


    else:

        label_text = ctk.CTkLabel(messagebox,
            width = 0,
            height = 0,
            text = text_,
            font = ('Inter', 18, 'bold'),
            wraplength = 260
        )

        label_text.pack(fill = 'x', pady = (20, 0))
        messagebox.pack_propagate(False)

        entry_email = ctk.CTkEntry(messagebox,
            width = 200,
            height = 25,
            font = ('DejaVu Sans Condensed', 10),
            border_width = 1,
            corner_radius = 5
        )

        entry_email.pack(pady = (5, 0))

        label_error = ctk.CTkLabel(messagebox,
            width = 0,
            height = 0,
            text = 'Preencha o campo solicitado.',
            font = ('DejaVu Sans Condensed', 8, 'bold'),
            text_color = 'red'
        )


        def button_close_window():

            global messagebox

            messagebox.destroy()
            messagebox = None


        def button_click():


            if entry_email.get() == '':

                label_error.pack(pady = (2, 0), before = button_ok)

                return

            else:

                label_text.configure(text = 'Uma senha de recuperação foi enviada ao seu e-mail',
                    font = ('Inter', 18, 'bold'),
                    wraplength = 260
                )

                label_error.destroy()
                entry_email.destroy()

                button_ok.pack_configure(pady = (25, 0))
                button_ok.configure(command = button_close_window)


        button_ok = ctk.CTkButton(messagebox,
            width = 100,
            height = 25,
            text = 'Ok',
            cursor = 'hand2',
            font = ('Inter', 14, 'bold'),
            text_color = 'white',
            fg_color = '#5d3452',
            hover_color = '#754363',
            corner_radius = 5,
            command = button_click
        )

        button_ok.pack(pady = (15, 0))