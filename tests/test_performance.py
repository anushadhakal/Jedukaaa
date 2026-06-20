import time
import pytest


class TestPerformance:

    # TC40
    def test_homepage_loads_within_10_seconds(self, driver):
        start = time.time()
        driver.get("https://www.jeduka.com/")
        driver.execute_script("return document.readyState")

        # Wait for page to fully load
        while driver.execute_script("return document.readyState") != "complete":
            time.sleep(0.5)

        end = time.time()
        load_time = end - start

        print(f"\nHomepage Load Time: {load_time:.2f} seconds")
        assert load_time < 10, f"Homepage took too long to load: {load_time:.2f} seconds"

    # TC40 (Register)
    def test_register_page_loads_within_10_seconds(self, driver):
        start = time.time()
        driver.get("https://www.jeduka.com/register.html")

        while driver.execute_script("return document.readyState") != "complete":
            time.sleep(0.5)

        end = time.time()
        load_time = end - start

        print(f"\nRegister Page Load Time: {load_time:.2f} seconds")
        assert load_time < 10, f"Register page took too long to load: {load_time:.2f} seconds"

    # TC41
    def test_performance_using_navigation_timing_api(self, driver):
        driver.get("https://www.jeduka.com/")

        while driver.execute_script("return document.readyState") != "complete":
            time.sleep(0.5)

        timing = driver.execute_script("""
            var t = window.performance.timing;
            return {
                full_load: t.loadEventEnd - t.navigationStart,
                dns_lookup: t.domainLookupEnd - t.domainLookupStart,
                server_response: t.responseEnd - t.requestStart,
                dom_interactive: t.domInteractive - t.navigationStart
            };
        """)

        full_load = timing["full_load"]
        dns_lookup = timing["dns_lookup"]
        server_response = timing["server_response"]
        dom_interactive = timing["dom_interactive"]

        print("\n")
        print("=" * 50)
        print("  PERFORMANCE REPORT — jeduka.com Homepage")
        print("=" * 50)
        print(f"  Full Page Load Time : {full_load} ms")
        print(f"  DNS Lookup Time     : {dns_lookup} ms")
        print(f"  Server Response Time: {server_response} ms")
        print(f"  DOM Interactive     : {dom_interactive} ms")
        print("=" * 50)

        assert full_load < 15000, f"Page took too long: {full_load} ms (limit: 15000 ms)"
        assert full_load > 0, "Navigation Timing API returned invalid value"
