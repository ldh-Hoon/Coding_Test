def solution(genres, plays):
    genre_play_count = {}
    song_info = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if genre not in genre_play_count:
            genre_play_count[genre] = 0
            song_info[genre] = []
        
        genre_play_count[genre] += play
        song_info[genre].append((i, play))
    sorted_genres = sorted(genre_play_count.items(), key=lambda x: -x[1])

    answer = []

    for genre, _ in sorted_genres:

        sorted_songs = sorted(song_info[genre], key=lambda x: (-x[1], x[0]))

        for i in range(min(2, len(sorted_songs))):
            answer.append(sorted_songs[i][0])

    return answer