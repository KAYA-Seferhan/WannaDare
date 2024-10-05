import tkinter
from PIL import Image, ImageTk
import pygame
import rounds
import random

cartridge_stack = []

shots_fired = 0

shells_ejected = 0

is_music_playing = False

main_window = tkinter.Tk()
main_window.title("Wanna DARE!?")
main_window.geometry("1200x800")
main_window.iconbitmap("assets\\icon.ico")
main_window.config(background="#242424")
main_window.resizable(False, False)

def start_gui():
    intro_screen()
    main_window.mainloop()

def dealer():
    if 1 <= random.randint(1, total_cartridge_count) <= live_cartridge_count.get():
        shotgun_to_player()

    else:
        shotgun_to_dealer()

turn = tkinter.StringVar()

stage_label_text = tkinter.StringVar()

dealer_health_count = tkinter.IntVar()
player_health_count = tkinter.IntVar()

dealer_health_label = tkinter.Label()
dealer_health_label_text = tkinter.StringVar()

player_health_label = tkinter.Label()
player_health_label_text = tkinter.StringVar()

live_cartridge_count = tkinter.IntVar()
blank_cartridge_count = tkinter.IntVar()
total_cartridge_count = blank_cartridge_count.get() + live_cartridge_count.get()

pygame.mixer.init()

bad_guy_image = Image.open("assets\\bad_guy.png")
bad_guy_photo = ImageTk.PhotoImage(bad_guy_image)

play_pause_image = Image.open("assets\\play_pause.png")
play_pause_photo = ImageTk.PhotoImage(play_pause_image)

big_play_pause_image = Image.open("assets\\big_play_pause.png")
big_play_pause_photo = ImageTk.PhotoImage(big_play_pause_image)

rewind_image = Image.open("assets\\rewind.png")
rewind_photo = ImageTk.PhotoImage(rewind_image)

big_rewind_image = Image.open("assets\\big_rewind.png")
big_rewind_photo = ImageTk.PhotoImage(big_rewind_image)

decadence_image = Image.open("assets\\decadence.png")
decadence_photo = ImageTk.PhotoImage(decadence_image)

piercing_light_image = Image.open("assets\\piercing_light.png")
piercing_light_photo = ImageTk.PhotoImage(piercing_light_image)

dare_image = Image.open("assets\\dare.png")
dare_photo = ImageTk.PhotoImage(dare_image)

how_to_play_image = Image.open("assets\\how_to_play.png")
how_to_play_photo = ImageTk.PhotoImage(how_to_play_image)

quit_image = Image.open("assets\\quit.png")
quit_photo = ImageTk.PhotoImage(quit_image)

do_it_image = Image.open("assets\\do_it.png")
do_it_photo = ImageTk.PhotoImage(do_it_image)

can_image = Image.open("assets\\can.png")
can_photo = ImageTk.PhotoImage(can_image)

can_t_image = Image.open("assets\\can_t.png")
can_t_photo = ImageTk.PhotoImage(can_t_image)

exit_confirm_image = Image.open("assets\\exit_confirm.png")
exit_confirm_photo = ImageTk.PhotoImage(exit_confirm_image)

fight_image = Image.open("assets\\fight.png")
fight_photo = ImageTk.PhotoImage(fight_image)

give_up_image = Image.open("assets\\give_up.png")
give_up_photo = ImageTk.PhotoImage(give_up_image)

you_image = Image.open("assets\\you.png")
you_photo = ImageTk.PhotoImage(you_image)

dealer_image = Image.open("assets\\dealer.png")
dealer_photo = ImageTk.PhotoImage(dealer_image)

shotgun_image = Image.open("assets\\shotgun.png")
shotgun_photo = ImageTk.PhotoImage(shotgun_image)

def set_music_volume_25():
    pygame.mixer.music.set_volume(0.25)

def set_music_volume_50():
    pygame.mixer.music.set_volume(0.5)

def set_music_volume_75():
    pygame.mixer.music.set_volume(0.75)

def set_music_volume_100():
    pygame.mixer.music.set_volume(1)

def clear_window(where):
    for widget in where.winfo_children():
        widget.destroy()

def intro_screen():
    clear_window(main_window)

    def fade_in(steps=200, duration=7250):
        intro_logo_image = Image.open("assets\\SierraKilo_Games.png").convert("RGBA")
        width, height = intro_logo_image.size
        blank_image = Image.new("RGBA", (width, height), (255, 255, 255, 0))

        delay = duration // steps

        def update_photo(step=0):
            if step <= steps:
                blended_image = Image.blend(blank_image, intro_logo_image, alpha=step/steps)
                intro_logo_photo = ImageTk.PhotoImage(blended_image)

                intro_canvas.create_image(600, 400, image=intro_logo_photo)

                intro_canvas.image = intro_logo_photo

                main_window.after(delay, update_photo, step + 1)

            else:
                main_window.after(11500)
                main_menu()

        update_photo()

    intro_canvas = tkinter.Canvas(main_window)
    intro_canvas.config(background="#242424")
    intro_canvas.place(x=0, y=0, width=1200, height=800)

    fade_in()

    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.load("assets\\THX_intro.mp3")
    pygame.mixer.music.play()

def play_pause_music():
    global is_music_playing
    if is_music_playing:
        pygame.mixer.music.pause()
        is_music_playing = False

    else:
        pygame.mixer.music.unpause()
        is_music_playing = True

def rewind_music():
    global is_music_playing
    pygame.mixer.music.play(-1)
    is_music_playing = True

def main_menu():
    clear_window(main_window)

    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.load("assets\\Disturbed-Decadence.mp3")
    pygame.mixer.music.play(-1)
    global is_music_playing
    is_music_playing = True

    main_label = tkinter.Label(main_window)
    main_label.config(image=bad_guy_photo, background="#242424")
    main_label.place(x=0, y=0, width=1200, height=800)

    dare_button = tkinter.Button(main_label)
    dare_button.config(image=dare_photo, command=lambda: [stage_1()], background="#242424", relief="flat", border=0, activebackground="#242424")
    dare_button.place(x=410, y=550, width=380, height=100)

    how_to_play_button = tkinter.Button(main_label)
    how_to_play_button.config(image=how_to_play_photo, command=how_to_play_screen, background="#242424", relief="flat", border=0, activebackground="#242424")
    how_to_play_button.place(x=440, y=675, width=320, height=30)

    quit_button = tkinter.Button(main_label)
    quit_button.config(image=quit_photo, command=exit_confirm, background="#242424", relief="flat", border=0, activebackground="#242424")
    quit_button.place(x=545, y=725, width=110, height=30)

    music_name_label = tkinter.Label(main_label)
    music_name_label.config(image=decadence_photo, background="#242424")
    music_name_label.place(x=1015, y=780, width=176, height=10)

    music_play_pause_button = tkinter.Button(main_label)
    music_play_pause_button.config(image=play_pause_photo, command=play_pause_music, background="#242424", relief="flat", border=0, activebackground="#242424")
    music_play_pause_button.place(x=1015, y=760, width=30, height=15)

    music_rewind_button = tkinter.Button(main_label)
    music_rewind_button.config(image=rewind_photo, command=rewind_music, background="#242424", relief="flat", border=0, activebackground="#242424")
    music_rewind_button.place(x=1060, y=760, width=15, height=15)

    seperator_label = tkinter.Label(main_label)
    seperator_label.config(text="|", foreground="white", font=("Arial", 10, "bold"), background="#242424")
    seperator_label.place(x=1080, y=760, width=5, height=15)

    set_music_volume_100_button = tkinter.Button(main_label)
    set_music_volume_100_button.config(text="100", foreground="white", font=("Arial", 10, "bold"), command=set_music_volume_100, background="#242424", relief="flat", border=0, activebackground="#242424")
    set_music_volume_100_button.place(x=1165, y=760, width=25, height=15)

    set_music_volume_75_button = tkinter.Button(main_label)
    set_music_volume_75_button.config(text="75", foreground="white", font=("Arial", 10, "bold"), command=set_music_volume_75, background="#242424", relief="flat", border=0, activebackground="#242424")
    set_music_volume_75_button.place(x=1140, y=760, width=15, height=15)

    set_music_volume_50_button = tkinter.Button(main_label)
    set_music_volume_50_button.config(text="50", foreground="white", font=("Arial", 10, "bold"), command=set_music_volume_50, background="#242424", relief="flat", border=0, activebackground="#242424")
    set_music_volume_50_button.place(x=1115, y=760, width=15, height=15)

    set_music_volume_25_button = tkinter.Button(main_label)
    set_music_volume_25_button.config(text="25", foreground="white", font=("Arial", 10, "bold"), command=set_music_volume_25, background="#242424", relief="flat", border=0, activebackground="#242424")
    set_music_volume_25_button.place(x=1090, y=760, width=15, height=15)

def dare():
    clear_window(main_window)

    pygame.mixer.music.stop()
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.load("assets\\Piercing_Light_(Mako_Remix)-League_of_Legends.mp3")
    pygame.mixer.music.play(-1)
    global is_music_playing
    is_music_playing = True

    main_frame = tkinter.Frame(main_window)
    main_frame.config(background="#242424", highlightthickness=1, highlightbackground="white")
    main_frame.place(x=1, y=1, width=1198, height=798)

    dealer_button = tkinter.Button(main_frame)
    dealer_button.config(image=dealer_photo, command=shotgun_to_dealer, background="#242424", relief="flat", border=0, activebackground="#242424")
    dealer_button.place(x=180, y=15, width=435, height=75)

    you_button = tkinter.Button(main_frame)
    you_button.config(image=you_photo, command=shotgun_to_player, background="#242424", relief="flat", border=0, activebackground="#242424")
    you_button.place(x=285, y=715, width=225, height=75)

    table_frame = tkinter.Frame(main_frame)
    table_frame.config(background="#242424", highlightthickness=1, highlightbackground="white")
    table_frame.place(x=25, y=100, width=750, height=600)

    dealer_table_frame = tkinter.Frame(table_frame)
    dealer_table_frame.config(background="dark green", highlightthickness=1, highlightbackground="white")
    dealer_table_frame.place(x=-1, y=-1, width=750, height=300)

    player_table_frame = tkinter.Frame(table_frame)
    player_table_frame.config(background="dark green", highlightthickness=1, highlightbackground="white")
    player_table_frame.place(x=-1, y=298, width=750, height=301)

    shotgun_frame = tkinter.Frame(table_frame)
    shotgun_frame.config(background="dark green", highlightthickness=1, highlightbackground="white")
    shotgun_frame.place(x=94, y=245, width=562, height=110)

    shotgun_button = tkinter.Button(shotgun_frame)
    shotgun_button.config(image=shotgun_photo, background="#242424", relief="flat", border=0, activebackground="#242424", highlightthickness=10, highlightbackground="white")
    shotgun_button.place(x=0, y=0, width=560, height=108)

    controls_frame = tkinter.Frame(main_frame)
    controls_frame.config(background="#242424", highlightthickness=1, highlightbackground="white")
    controls_frame.place(x=800, y=-1, width=397, height=798)

    stage_label = tkinter.Label(controls_frame)
    stage_label.config(textvariable=stage_label_text, foreground="white",font=("Script MT Bold", 30, "bold"), background="#242424", relief="flat", border=0, activebackground="#242424")
    stage_label.place(x=100, y=50, width=200, height=50)

    global dealer_health_label
    dealer_health_label = tkinter.Label(controls_frame)
    dealer_health_label.config(text="DEALER: ", foreground="white", anchor="w", font=("SimSun", 20, "bold"), background="#242424", relief="flat", border=0, activebackground="#242424")
    dealer_health_label.place(x=50, y=150, width=325, height=30)

    global dealer_health_label_text
    dealer_health_label = tkinter.Label(controls_frame)
    dealer_health_label.config(textvariable=dealer_health_label_text, foreground="white", anchor="w", font=("SimSun", 20, "bold"), background="#242424", relief="flat", border=0, activebackground="#242424")
    dealer_health_label.place(x=165, y=147, width=200, height=30)

    global player_health_label
    player_health_label = tkinter.Label(controls_frame)
    player_health_label.config(text="PLAYER: ", foreground="white", anchor="w", font=("SimSun", 20, "bold"), background="#242424", relief="flat", border=0, activebackground="#242424")
    player_health_label.place(x=50, y=200, width=325, height=30)

    global player_health_label_text
    player_health_label_variable = tkinter.Label(controls_frame)
    player_health_label_variable.config(textvariable=player_health_label_text, foreground="white", anchor="w", font=("SimSun", 20, "bold"), background="#242424", relief="flat", border=0, activebackground="#242424")
    player_health_label_variable.place(x=165, y=197, width=200, height=30)

    live_cartridge_count_label = tkinter.Label(controls_frame)
    live_cartridge_count_label.config(text="LIVE:  x", foreground="white", anchor="w", font=("SimSun", 20, "bold italic"), background="#242424", relief="flat", border=0, activebackground="#242424")
    live_cartridge_count_label.place(x=50, y=300, width=325, height=30)

    global live_cartridge_count
    live_cartridge_count_label = tkinter.Label(controls_frame)
    live_cartridge_count_label.config(textvariable=live_cartridge_count, foreground="white", anchor="w", font=("SimSun", 20, "bold italic"), background="#242424", relief="flat", border=0, activebackground="#242424")
    live_cartridge_count_label.place(x=175, y=300, width=200, height=30)

    blank_cartridge_count_label = tkinter.Label(controls_frame)
    blank_cartridge_count_label.config(text="BLANK: x", foreground="white", anchor="w", font=("SimSun", 20, "bold italic"), background="#242424", relief="flat", border=0, activebackground="#242424")
    blank_cartridge_count_label.place(x=50, y=350, width=325, height=30)

    global blank_cartridge_count
    blank_cartridge_count_label = tkinter.Label(controls_frame)
    blank_cartridge_count_label.config(textvariable=blank_cartridge_count, foreground="white", anchor="w", font=("SimSun", 20, "bold italic"), background="#242424", relief="flat", border=0, activebackground="#242424")
    blank_cartridge_count_label.place(x=175, y=350, width=200, height=30)

    music_controls_frame = tkinter.Frame(controls_frame)
    music_controls_frame.config(background="#242424", highlightthickness=1, highlightbackground="white")
    music_controls_frame.place(x=-1, y=599, width=397, height=198)

    music_name_label = tkinter.Label(music_controls_frame)
    music_name_label.config(image=piercing_light_photo, background="#242424")
    music_name_label.place(x=45, y=100, width=308, height=60)

    music_play_pause_button = tkinter.Button(music_controls_frame)
    music_play_pause_button.config(image=big_play_pause_photo, command=play_pause_music, background="#242424", relief="flat", border=0, activebackground="#242424")
    music_play_pause_button.place(x=40, y=40, width=60, height=30)

    music_rewind_button = tkinter.Button(music_controls_frame)
    music_rewind_button.config(image=big_rewind_photo, command=rewind_music, background="#242424", relief="flat", border=0, activebackground="#242424")
    music_rewind_button.place(x=115, y=40, width=30, height=30)

    seperator_label = tkinter.Label(music_controls_frame)
    seperator_label.config(text="|", foreground="white", font=("Arial", 20, "bold"), background="#242424")
    seperator_label.place(x=155, y=40, width=10, height=30)

    set_music_volume_100_button = tkinter.Button(music_controls_frame)
    set_music_volume_100_button.config(text="100", foreground="white", font=("Arial", 20, "bold"), command=set_music_volume_100, background="#242424", relief="flat", border=0, activebackground="#242424")
    set_music_volume_100_button.place(x=310, y=40, width=50, height=30)

    set_music_volume_75_button = tkinter.Button(music_controls_frame)
    set_music_volume_75_button.config(text="75", foreground="white", font=("Arial", 20, "bold"), command=set_music_volume_75, background="#242424", relief="flat", border=0, activebackground="#242424")
    set_music_volume_75_button.place(x=265, y=40, width=30, height=30)

    set_music_volume_50_button = tkinter.Button(music_controls_frame)
    set_music_volume_50_button.config(text="50", foreground="white", font=("Arial", 20, "bold"), command=set_music_volume_50, background="#242424", relief="flat", border=0, activebackground="#242424")
    set_music_volume_50_button.place(x=220, y=40, width=30, height=30)

    set_music_volume_25_button = tkinter.Button(music_controls_frame)
    set_music_volume_25_button.config(text="25", foreground="white", font=("Arial", 20, "bold"), command=set_music_volume_25, background="#242424", relief="flat", border=0, activebackground="#242424")
    set_music_volume_25_button.place(x=175, y=40, width=30, height=30)

    global turn

    def dealer_move(*args):
        if turn.get() == "dealer":
            main_window.after(15000, dealer)

    turn.trace_add("write", dealer_move)

def health_label_creator(no):
    player_health_label_text.set("")
    dealer_health_label_text.set("")

    x = 1
    while x<= no:
        temp_var = player_health_label_text.get()
        temp_var = temp_var + "🗲"
        player_health_label_text.set(temp_var)

        temp_var2 = dealer_health_label_text.get()
        temp_var2 = temp_var2 + "🗲"
        dealer_health_label_text.set(temp_var2)

        x = x + 1

def update_player_health_text():
    global player_health_label_text
    var1 = player_health_label_text.get()
    var1 = var1[:-1]
    player_health_label_text.set(var1)

def stage(no):
    global stage_label_text
    black_screen = tkinter.Frame(main_window)
    black_screen.config(background="black")
    black_screen.place(x=0, y=0, width=1200, height=800)

    if no == "Final":
        note_label = tkinter.Label(black_screen)
        note_label.config(text="Final Stage", foreground="white", font=("Script MT Bold", 45, "bold italic"), background="black")
        main_window.after(500, lambda: [note_label.place(x=100, y=350, width=1000, height=100)])
        main_window.after(3000, lambda: [black_screen.destroy()])
        stage_label_text.set("Final Stage")
        main_window.after(3000, lambda: [dare()])
    else:
        note_label = tkinter.Label(black_screen)
        note_label.config(text=f"Stage {no}", foreground="white", font=("Script MT Bold", 45, "bold italic"), background="black")
        main_window.after(500, lambda: [note_label.place(x=100, y=350, width=1000, height=100)])
        main_window.after(3000, lambda: [black_screen.destroy()])
        stage_label_text.set(f"Stage {no}")
        main_window.after(3000, lambda: [dare()])

def stage_1():
    def next_stage(*args):
        if dealer_health_count.get() == 0:
            stage_2()
        if player_health_count.get() == 0:
            stage_1()

    global dealer_health_count
    global player_health_count
    dealer_health_count.set(2)
    player_health_count.set(2)

    load_cartridges(3)

    live_cartridge_count.set(3)
    blank_cartridge_count.set(6)

    health_label_creator(2)

    stage(1)

    dealer_health_count.trace_add("write", next_stage)
    player_health_count.trace_add("write", next_stage)

def stage_2():
    def next_stage(*args):
        if dealer_health_count.get() == 0:
            stage_3()
        if player_health_count.get() == 0:
            stage_2()

    global dealer_health_count
    global player_health_count
    dealer_health_count.set(3)
    player_health_count.set(3)

    load_cartridges(5)

    live_cartridge_count.set(5)
    blank_cartridge_count.set(10)

    health_label_creator(3)

    stage(2)

    dealer_health_count.trace_add("write", next_stage)
    player_health_count.trace_add("write", next_stage)

def stage_3():
    def next_stage(*args):
        if dealer_health_count.get() == 0:
            final_stage()
        if player_health_count.get() == 0:
            stage_3()

    global dealer_health_count
    global player_health_count
    dealer_health_count.set(4)
    player_health_count.set(4)

    load_cartridges(7)

    live_cartridge_count.set(7)
    blank_cartridge_count.set(14)

    health_label_creator(4)

    stage(3)

    dealer_health_count.trace_add("write", next_stage)
    player_health_count.trace_add("write", next_stage)

def final_stage():
    def next_stage(*args):
        if dealer_health_count.get() == 0:
            stage_2()
        if player_health_count.get() == 0:
            stage_1()

    global dealer_health_count
    global player_health_count
    dealer_health_count.set(5)
    player_health_count.set(5)

    load_cartridges(9)

    live_cartridge_count.set(9)
    blank_cartridge_count.set(18)

    health_label_creator(5)

    stage("Final")

    dealer_health_count.trace_add("write", next_stage)
    player_health_count.trace_add("write", next_stage)

def bang(turn_parameter, is_self_attack):
    black_screen = tkinter.Frame(main_window)
    black_screen.config(background="black")
    black_screen.place(x=0, y=0, width=1200, height=800)

    if turn_parameter == "dealer":
        if is_self_attack:
            note_label = tkinter.Label(black_screen)
            note_label.config(text="The Dealer pointed the shotgun at his own face...", foreground="#242424", font=("Script MT Bold", 45, "bold italic"), background="black")
            main_window.after(250, lambda: [note_label.place(x=25, y=350, width=1150, height=100)])
            main_window.after(3150, lambda: [note_label.config(foreground="red")])

        else:
            note_label = tkinter.Label(black_screen)
            note_label.config(text="The Dealer pointed the shotgun at your face...", foreground="#242424", font=("Script MT Bold", 45, "bold italic"), background="black")
            main_window.after(250, lambda: [note_label.place(x=25, y=350, width=1150, height=100)])
            main_window.after(3150, lambda: [note_label.config(foreground="red")])

    elif turn_parameter == "player":
        if is_self_attack:
            note_label = tkinter.Label(black_screen)
            note_label.config(text="You pointed the shotgun at your own face...", foreground="#242424", font=("Script MT Bold", 45, "bold italic"), background="black")
            main_window.after(250, lambda: [note_label.place(x=25, y=350, width=1150, height=100)])
            main_window.after(3150, lambda: [note_label.config(foreground="red")])

        else:
            note_label = tkinter.Label(black_screen)
            note_label.config(text="You pointed the shotgun at The Dealer's face...", foreground="#242424", font=("Script MT Bold", 45, "bold italic"), background="black")
            main_window.after(250, lambda: [note_label.place(x=25, y=350, width=1150, height=100)])
            main_window.after(3150, lambda: [note_label.config(foreground="red")])

    bang_sound = pygame.mixer.Sound("assets\\bang.mp3")
    bang_sound.set_volume(1)

    bep_bep_sound = pygame.mixer.Sound("assets\\bep_bep.mp3")
    bep_bep_sound.set_volume(1)

    shock_sound = pygame.mixer.Sound("assets\\shock.mp3")
    shock_sound.set_volume(1)

    heartbeat_sound = pygame.mixer.Sound("assets\\heartbeat.mp3")
    heartbeat_sound.set_volume(1)

    main_window.after(2850, pygame.mixer.music.pause)
    main_window.after(3000, bang_sound.play)
    main_window.after(6500, bep_bep_sound.play)
    main_window.after(9750, shock_sound.play)
    main_window.after(16000, heartbeat_sound.play)
    main_window.after(16000, pygame.mixer.music.play)
    main_window.after(18250, black_screen.destroy)

def click(turn_parameter, is_self_attack):
    black_screen = tkinter.Frame(main_window)
    black_screen.config(background="black")
    black_screen.place(x=0, y=0, width=1200, height=800)

    if turn_parameter == "dealer":
        if is_self_attack:
            note_label = tkinter.Label(black_screen)
            note_label.config(text="The Dealer pointed the shotgun at his own face...", foreground="#242424", font=("Script MT Bold", 45, "bold italic"), background="black")
            main_window.after(250, lambda: [note_label.place(x=25, y=350, width=1150, height=100)])
            main_window.after(3000, lambda: [note_label.config(foreground="white")])

        else:
            note_label = tkinter.Label(black_screen)
            note_label.config(text="The Dealer pointed the shotgun at your face...", foreground="#242424", font=("Script MT Bold", 45, "bold italic"), background="black")
            main_window.after(250, lambda: [note_label.place(x=25, y=350, width=1150, height=100)])
            main_window.after(3000, lambda: [note_label.config(foreground="white")])

    elif turn_parameter == "player":
        if is_self_attack:
            note_label = tkinter.Label(black_screen)
            note_label.config(text="You pointed the shotgun at your own face...", foreground="#242424", font=("Script MT Bold", 45, "bold italic"), background="black")
            main_window.after(250, lambda: [note_label.place(x=25, y=350, width=1150, height=100)])
            main_window.after(3000, lambda: [note_label.config(foreground="white")])

        else:
            note_label = tkinter.Label(black_screen)
            note_label.config(text="You pointed the shotgun at The Dealer's face...", foreground="#242424", font=("Script MT Bold", 45, "bold italic"), background="black")
            main_window.after(250, lambda: [note_label.place(x=25, y=350, width=1150, height=100)])
            main_window.after(3000, lambda: [note_label.config(foreground="white")])

    main_window.after(2500, pygame.mixer.music.set_volume, 0.05)
    click_sound = pygame.mixer.Sound("assets\\click.mp3")
    click_sound.set_volume(1)
    main_window.after(3000, click_sound.play)
    main_window.after(3500, pygame.mixer.music.set_volume, 0.25)
    main_window.after(6000, black_screen.destroy)

def how_to_play_screen():
    clear_window(main_window)

    pygame.mixer.music.stop()
    pygame.mixer.music.load("assets\\suspense.mp3")
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1)

    how_to_play_label = tkinter.Label(main_window)
    how_to_play_label.config(image=do_it_photo, background="#242424")
    how_to_play_label.place(x=0, y=0, width=1200, height=800)

    can_button = tkinter.Button(how_to_play_label)
    can_button.config(image=can_photo, command=main_menu, background="#242424", relief="flat", border=0, activebackground="#242424")
    can_button.place(x=200, y=600, width=285, height=75)

    can_t_button = tkinter.Button(how_to_play_label)
    can_t_button.config(image=can_t_photo, command=exit_confirm, background="#242424", relief="flat", border=0, activebackground="#242424")
    can_t_button.place(x=650, y=600, width=375, height=75)

def exit_confirm():
    clear_window(main_window)

    pygame.mixer.music.stop()
    pygame.mixer.music.load("assets\\suspense.mp3")
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1)

    exit_confirm_label = tkinter.Label(main_window)
    exit_confirm_label.config(image=exit_confirm_photo, background="#242424")
    exit_confirm_label.place(x=0, y=0, width=1200, height=800)

    fight_button = tkinter.Button(exit_confirm_label)
    fight_button.config(image=fight_photo, command=main_menu, background="#242424", relief="flat", border=0, activebackground="#242424")
    fight_button.place(x=150, y=600, width=330, height=75)

    give_up_button = tkinter.Button(exit_confirm_label)
    give_up_button.config(image=give_up_photo, command=main_window.destroy, background="#242424", relief="flat", border=0, activebackground="#242424")
    give_up_button.place(x=650, y=600, width=450, height=75)

main_window.protocol("WM_DELETE_WINDOW", exit_confirm)

def closing():
    black_screen = tkinter.Frame(main_window)
    black_screen.config(background="black")
    black_screen.place(x=0, y=0, width=1200, height=800)

    note_label = tkinter.Label(black_screen)
    note_label.config(text="Thanks for playing...", foreground="#242424", font=("Script MT Bold", 45, "bold italic"), background="black")
    main_window.after(500, lambda: [note_label.place(x=100, y=350, width=1000, height=100)])
    main_window.after(2000, lambda: [black_screen.destroy(), main_window.destroy()])
















def load_cartridges(live_cartridge_count_parameter):
    global cartridge_stack
    global total_cartridge_count
    global live_cartridge_count
    global blank_cartridge_count
    live_cartridge_count.set(live_cartridge_count_parameter)
    blank_cartridge_count.set(live_cartridge_count.get() * 2)
    total_cartridge_count = live_cartridge_count.get() + blank_cartridge_count.get()

    x = 1
    live_cartridge_counter = 0
    blank_cartridge_counter = 0
    while x <= total_cartridge_count:
        process = random.randint(1,100)

        if 1 <= process <= 50:
            if live_cartridge_counter < live_cartridge_count.get():
                cartridge_object = rounds.Cartridge(True)
                cartridge_stack.append(cartridge_object)
                live_cartridge_counter = live_cartridge_counter + 1
            else:
                cartridge_object = rounds.Cartridge(False)
                cartridge_stack.append(cartridge_object)
                blank_cartridge_counter = blank_cartridge_counter + 1

        if 50 < process <= 100:
            if blank_cartridge_counter < blank_cartridge_count.get():
                cartridge_object = rounds.Cartridge(False)
                cartridge_stack.append(cartridge_object)
                blank_cartridge_counter = blank_cartridge_counter + 1
            else:
                cartridge_object = rounds.Cartridge(True)
                cartridge_stack.append(cartridge_object)
                live_cartridge_counter = live_cartridge_counter + 1

        x = x + 1

def shotgun_to_dealer():
    global turn
    global cartridge_stack
    global live_cartridge_count
    global blank_cartridge_count
    global total_cartridge_count
    global dealer_health_count
    global dealer_health_label_text
    cartridge_object = cartridge_stack.pop()

    is_self_attack = False

    if turn.get() == "dealer":
        is_self_attack = True

    elif turn.get() == "player":
        is_self_attack = False

    cartridge_object.show_cartridge_specs()

    if cartridge_object.is_live:
        bang(turn.get(), is_self_attack)
        live_cartridge_count.set(live_cartridge_count.get() - 1)
        total_cartridge_count = live_cartridge_count.get() + blank_cartridge_count.get()

        dealer_health_count.set(dealer_health_count.get() - 1)
        dealer_health_label_text.set(dealer_health_label_text.get()[:-1])

        if turn.get() == "player":
            turn.set("dealer")
        elif turn.get() == "dealer":
            turn.set("player")
    else:
        click(turn.get(), is_self_attack)
        blank_cartridge_count.set(blank_cartridge_count.get() - 1)
        total_cartridge_count = live_cartridge_count.get() + blank_cartridge_count.get()
        turn.set("dealer")

def shotgun_to_player():
    global live_cartridge_count
    global blank_cartridge_count
    global total_cartridge_count
    global player_health_count
    global turn
    global cartridge_stack
    global player_health_label_text
    cartridge_object = cartridge_stack.pop()

    is_self_attack = False

    if turn.get() == "dealer":
        is_self_attack = False
    elif turn.get() == "player":
        is_self_attack = True

    cartridge_object.show_cartridge_specs()

    if cartridge_object.is_live:
        bang(turn.get(), is_self_attack)
        live_cartridge_count.set(live_cartridge_count.get() - 1)
        total_cartridge_count = live_cartridge_count.get() + blank_cartridge_count.get()

        player_health_count.set(player_health_count.get() - 1)
        player_health_label_text.set(player_health_label_text.get()[:-1])

        if turn.get() == "player":
            turn.set("dealer")
        elif turn.get() == "dealer":
            turn.set("player")
    else:
        click(turn.get(), is_self_attack)
        blank_cartridge_count.set(blank_cartridge_count.get() - 1)
        total_cartridge_count = live_cartridge_count.get() + blank_cartridge_count.get()
        turn.set("player")

if __name__ == "__main__":
    start_gui()
