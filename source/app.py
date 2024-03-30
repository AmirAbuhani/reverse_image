import time
from single_thread import single_thread_reverse_img
from multiple_threads import multiple_threads_reverse_img


def write_results_to_file(txt):
    with open("performance_results.txt", "a") as file:
        data = file.write(f"{txt}\n")


def main():
    start_single_thread = time.perf_counter()
    single_thread_reverse_img()
    end_single_thread = time.perf_counter()
    total_time_single_thread = round(end_single_thread - start_single_thread, 2)
    text = f"In single thread, the reverse image has taken {total_time_single_thread} seconds."
    write_results_to_file(text)

    start_multiple_thread = time.perf_counter()
    multiple_threads_reverse_img()
    end_multiple_threads = time.perf_counter()
    total_time_multiple_threads = round(end_multiple_threads - start_multiple_thread, 2)
    text1 = f"In multiple threads, the reverse image has taken {total_time_multiple_threads} seconds."
    write_results_to_file(text1)


if __name__ == "__main__":
    main()
