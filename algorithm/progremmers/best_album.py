from collections import defaultdict

def solution(genres, plays):
    genres_played_dict = defaultdict(int)

    for genre, play in zip(genres, plays):
        genres_played_dict[genre] += play

    genre_ranks = [genre for genre, play in sorted(genres_played_dict.items(), key=lambda obj:obj[1], reverse=True)]

    play_idx_dict = defaultdict(list)
    for idx, genres_play_tuple in enumerate(zip(genres, plays)):
        play_idx_dict[genres_play_tuple[0]].append([genres_play_tuple[1], idx])

    answer = []
    for genre in genre_ranks:
        genre_rank_list = sorted(play_idx_dict[genre], key=lambda obj:obj[0], reverse=True)
        for idx, music in enumerate(genre_rank_list):
            if idx == 2:
                break
            answer.append(music[1])
    return answer