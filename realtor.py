from homeharvest import scrape_property
from datetime import datetime
import pandas as pd

def main():
  # Generate filename based on current timestamp
  current_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
  filename = f"HomeHarvest_{current_timestamp}.csv"

  properties = scrape_property(
    location="Cary, NC",
    listing_type="for_sale",  # or (for_sale, for_rent, pending)
    past_days=120,  # sold in last 30 days - listed in last 30 days if (for_sale, for_rent)
    property_type=['single_family','townhomes'],
    # date_from="2023-05-01", # alternative to past_days
    # date_to="2023-05-28",
    # foreclosure=True
    # mls_only=True,  # only fetch MLS listings
  )
  print(f"Number of properties: {len(properties)}")

  # Export to csv
  properties.to_csv(filename, index=False)
  print(properties.head())

if __name__ == "__main__":
    main()