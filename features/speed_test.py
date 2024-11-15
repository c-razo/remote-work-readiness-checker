import speedtest

def internet_speed_test():
    """
    Perform an internet speed test.
    """
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    results = {
        "Download Speed": f"{st.results.download / 1_000_000:.2f} Mbps",
        "Upload Speed": f"{st.results.upload / 1_000_000:.2f} Mbps",
        "Ping": f"{st.results.ping:.2f} ms"
    }
    return results

