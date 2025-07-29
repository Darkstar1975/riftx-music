import time

print("Tap any key to the beat. Press Enter to start and Ctrl+C to stop.") input("Ready? Press Enter to begin...")

import keyboard

beat_times = []

try: while True: keyboard.read_event(suppress=True) now = time.time() beat_times.append(now)

if len(beat_times) >= 2:
        intervals = [t - s for s, t in zip(beat_times[:-1], beat_times[1:])]
        avg_interval = sum(intervals) / len(intervals)
        bpm = 60 / avg_interval
        print(f"\rCurrent BPM: {bpm:.2f}", end="")

except KeyboardInterrupt: print("\nStopped.") if len(beat_times) >= 2: intervals = [t - s for s, t in zip(beat_times[:-1], beat_times[1:])] avg_interval = sum(intervals) / len(intervals) bpm = 60 / avg_interval print(f"Final BPM: {bpm:.2f}") else: print("Not enough taps recorded.")

