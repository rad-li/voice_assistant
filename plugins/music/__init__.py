"""
Плагин «Музыка и радио»

Ассистент включает музыку и онлайн радион. Путь к папке с музыкой можно изменить в переменной `path_to_music`
В `radio_channel` можно добавить свои ссылки на онлайн радио.

"""
__author__ = 'rad-li'
__version__ = 0.2

import random
import vlc
import os

# Инициализация VLC плеера
inst = vlc.Instance('--no-xlib -q > /dev/null 2>&1')
player = inst.media_player_new()
is_paused = False
musicIsPlayed = False
path_to_music = "music"

play_music = ['включи музыку', 'включи песню', 'музыка', 'музыку']
play_radio = ['радио', 'радиостанция', 'станция', 'следующее радио', 'следующая станция']
stop_music = ['стоп музыка', 'музыка стоп', 'стоп воспроизведение', 'останови музыку', 'выключи музыку', 'выключи радио']
next_track = ['следующий трек', 'следующая песня', 'следующее радио', 'следующая станция']

radio_channel = {
    "релакс": "https://pub0102.101.ru:8443/stream/trust/mp3/128/24?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrZXkiOiI4NTEwZDg2M2Y4NDhkZjZkNjg0MTExMmQ1NjliODUwNCIsIklQIjoiMzEuMzEuMTk2LjE5MyIsIlVBIjoiIiwiUmVmIjoiIiwidWlkX2NoYW5uZWwiOiIyNCIsInR5cGVfY2hhbm5lbCI6ImNoYW5uZWwiLCJ0eXBlRGV2aWNlIjoiUEMiLCJCcm93c2VyIjoiIiwiQnJvd3NlclZlcnNpb24iOiIiLCJTeXN0ZW0iOiJVbmtub3duIiwiZXhwIjoxNjk3MDkxNzg3fQ.7VLpzk33Z-QkFtzSY76dWur7TtlfANVjze8JGgyXkv0",
    "поп": "http://pub0302.101.ru:8000/stream/pro/aac/64/155?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpcCI6IjUxLjE1OC4xNDQuMzIiLCJ1c2VyYWdlbnQiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NjguMCkgR2Vja29cLzIwMTAwMTAxIEZpcmVmb3hcLzY4LjAiLCJ1aWRfY2hhbm5lbCI6IjE1NSIsInR5cGVfY2hhbm5lbCI6ImNoYW5uZWwiLCJleHAiOjE1OTYyNzM2NDh9.9nrmdE85O78l_SWG8ZIbcBb81rlMfjWEFZtyU54v240",
    "хипхоп": "http://pub0202.101.ru:8000/stream/pro/aac/64/8?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpcCI6IjUxLjE1OC4xNDQuMzIiLCJ1c2VyYWdlbnQiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NjguMCkgR2Vja29cLzIwMTAwMTAxIEZpcmVmb3hcLzY4LjAiLCJ1aWRfY2hhbm5lbCI6IjgiLCJ0eXBlX2NoYW5uZWwiOiJjaGFubmVsIiwiZXhwIjoxNTk2MjczNzM0fQ.CFeZY0sd_dE8A-Fb_cJDvmfoE03TfentLDYUNc2o5wY",
    "техно": "http://pub0202.101.ru:8000/stream/trust/mp3/128/18?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpcCI6IjUxLjE1OC4xNDQuMzIiLCJ1c2VyYWdlbnQiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NjguMCkgR2Vja29cLzIwMTAwMTAxIEZpcmVmb3hcLzY4LjAiLCJ1aWRfY2hhbm5lbCI6IjE4IiwidHlwZV9jaGFubmVsIjoiY2hhbm5lbCIsImV4cCI6MTU5NjI3NDIzM30.QgEVxowg5isL-Bx21mGRHlJtQVrlBMpPGMYedjxzAQM",
    "джаз": "http://pub0202.101.ru:8000/stream/pro/aac/128/85?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpcCI6IjUxLjE1OC4xNDQuMzIiLCJ1c2VyYWdlbnQiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NjguMCkgR2Vja29cLzIwMTAwMTAxIEZpcmVmb3hcLzY4LjAiLCJ1aWRfY2hhbm5lbCI6Ijg1IiwidHlwZV9jaGFubmVsIjoiY2hhbm5lbCIsImV4cCI6MTU5NjI3NDMzM30.qMRUJuGhdAWRkuWJ9l4NscxmsKy26y8q0risQrU_Nt0"}


def play_random_music():
    global musicIsPlayed, usrPlayer
    try:
        music_folder = path_to_music
    except FileNotFoundError:
        music_folder = path_to_music

    # Получение списка файлов из папки с музыкой
    playlist = os.listdir(music_folder)
    if musicIsPlayed:
        player.stop()
        media = inst.media_new(f"{music_folder}/{random.choice(playlist)}")
        player.set_media(media)
        player.play()
    else:
        # Воспроизведение музыки из указанной папки
        media = inst.media_new(f"{music_folder}/{random.choice(playlist)}")
        player.set_media(media)
        player.play()
        musicIsPlayed = True


def main(command):
    answer = ""
    for i in play_radio:
        if i in command and command not in stop_music:
            radiostation = command.replace(i, '')
            radiostation = radiostation.replace(" ", '')

            if radiostation == "":
                random_pair = random.choice(list(radio_channel.items()))
                random_name = random_pair[0]
                random_url = random_pair[1]

                answer = "Включаю радио " + random_name

                media = inst.media_new(random_url)
                player.set_media(media)
                player.play()

            else:
                answer = "Включаю радио " + radiostation
                for name, stream in radio_channel.items():
                    if radiostation in name:
                        media = inst.media_new(stream)
                        player.set_media(media)
                        player.play()

    for i in play_music:
        if i in command and command not in stop_music:
            command = command.replace(i, '')
            answer = "Включаю музыку"
            play_random_music()

    for i in stop_music:
        if i == command:
            answer = ""
            player.pause()  # Остановка проигрывателя

    for i in next_track:
        if i == command:
            answer = "Следующая песня"
            play_random_music()
            break

    return answer
