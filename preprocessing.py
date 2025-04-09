from pathlib import Path
from pydub import AudioSegment, silence


wav_directory = Path("dataset/wav_files")
output_directory = Path("dataset/clips")
output_directory.mkdir(exist_ok=True, parents=True)

for wav_file in wav_directory.rglob('*.wav'):
    print(f"Processing {wav_file.name}")
    audio = AudioSegment.from_wav(wav_file)
    audio = audio[5*60000: ] # Remove first 5 minutes

    non_silent = silence.detect_nonsilent(audio, min_silence_len=500, silence_thresh=-40)
    
    # Merge all non-silent segments
    merged_audio = AudioSegment.empty()
    for start, end in non_silent:
        merged_audio += audio[start:end]

        clip_length = 10 * 1000
        clips = []
        for i in range(0, len(merged_audio), clip_length):
             clip = merged_audio[i:i+clip_length]
             clips.append(clip)
             if len(clips) == 20:
                  break

    speaker_id = wav_file.stem.split('_')[-1]
    speaker_clip_dir = output_directory/speaker_id
    speaker_clip_dir.mkdir(exist_ok = True, parents=True)

    for idx, clip in enumerate(clips):
        clip.export(speaker_clip_dir/f"{speaker_id}_clip_{idx+1}.wav", format="wav")