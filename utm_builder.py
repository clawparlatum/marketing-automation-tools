def build_utm(base_url, source, medium, campaign):
    return f"{base_url}?utm_source={source}&utm_medium={medium}&utm_campaign={campaign}"

if __name__ == "__main__":
    url = build_utm(
        "https://example.com",
        "facebook",
        "cpc",
        "lead_campaign"
    )

    print(url)
