from datetime import datetime

def log(episode_num, msg):
    print(f'-- {now()} -- Episode {episode_num} -- {msg}')

def now():
    return datetime.now().strftime('%H:%M:%S')

def format_pub_date(pub_date):
    if pub_date is None:
        return 'the beginning of time'
    # Fri, 04 Mar 2020 20:56:53 +0000
    date = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %z")
    # Mar 04, 2020
    return date.strftime("%b %d, %Y")

def make_audio_file_path(episode_num):
    return f'audio/{episode_num}.mp3'

def is_new_episode(episode, last_episode_num):
    if hasattr(episode, 'itunes_episode'):
        return get_episode_num(episode) > last_episode_num

def get_episode_num(episode):
    return int(episode['itunes_episode'])

def is_audio(media):
    return media['medium'] == 'audio'

def get_audio_url(episode):
    audio, *_ = filter(is_audio, episode['media_content'])
    return audio['url']