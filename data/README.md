# data

All datasets used in the course live here. Lecture notebooks sit in a week folder next to this one,
so they load data with a path like:

```python
df = pd.read_excel("../data/mpg.xlsx")
```

This is why you need the folder structure from `ban405-workspace.zip` rather than just a loose
notebook. Relative paths, absolute paths and URLs are covered in full when we get to project
structure.

> 📝 **Note:** not every project is laid out this way. A project whose notebook sits at its own root,
> with `data/` beside it, uses `data/x.csv` with no `../`. Understanding *why* the two differ matters
> more than memorizing either one.

---

## What is here, and where it came from

| File | Rows × cols | Source |
|---|---|---|
| `co2_emissions.csv` | 6 240 × 11 | World Bank Open Data API — see below |
| `country_info.csv` | 295 × 4 | World Bank Open Data API — see below |
| `titanic.csv` | 891 × 7 | The Titanic passenger manifest, reduced to seven columns. Widely circulated; the version here matches the one used in [datasciencedojo/datasets](https://github.com/datasciencedojo/datasets) |
| `titanic_pipe.csv` | 891 × 7 | The same data, saved with `\|` as the separator instead of a comma |
| `AAPL.csv` | 252 × 7 | Daily Apple share prices for 2020, from Yahoo Finance |
| `NASDAQ.csv` | 13 842 × 2 | Daily closing level of the NASDAQ Composite index, 5 February 1971 to 30 December 2025. Taken unmodified from the [TECH2 course repository](https://github.com/richardfoltyn/TECH2-H26); the series matches FRED's [`NASDAQCOM`](https://fred.stlouisfed.org/series/NASDAQCOM), which is indexed to 100 on its first day |
| `stocks/` | 10 files, 252 × 7 each | Daily 2020 share prices for AAPL, AMZN, BABA, FB, GOOG, JNJ, JPM, MSFT, TSLA and WMT, from Yahoo Finance |
| `mpg.xlsx` | 398 × 8 | The Auto MPG dataset, [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/9/auto+mpg) |
| `FRED_annual.xlsx` | 70 × 6 | Annual US macroeconomic series, 1954–2023, from [FRED](https://fred.stlouisfed.org/) (St. Louis Fed) |
| `eurostat.xlsx` | 3 sheets; data is 38 × 24 | Annual electricity available for final consumption, GWh, 2001–2023, by country. [Eurostat](https://ec.europa.eu/eurostat) table `nrg_cb_e`, downloaded unmodified |
| `titanic.xlsx` | 891 × 7 | **Derived, not tracked.** The lecture notebook writes it from `titanic.csv`; if it is not here yet, run the notebook |
| `survey_data.csv` | 2 884 × 7 | A labor-market survey extract: earnings, schooling, experience, sex and sector. Colon-separated |

Two files are kept in their awkward original form on purpose, because reading an awkward file is part
of the job:

- **`eurostat.xlsx`** is exactly what Eurostat's export button produces. The workbook has three
  sheets and the data is not on the first one; above the table sit nine rows of extraction metadata;
  every second column is an empty flag column; the years run across the columns instead of down the
  rows; and the country list has EU-wide aggregates mixed in at the top. Opening it with default
  settings gives you nonsense, and that is the point.
- **`survey_data.csv`** uses `:` as its separator, so a default `read_csv` gives you one column with
  the entire header mashed into its name.

Two files here are **derived** rather than sources: `titanic_pipe.csv` and `titanic.xlsx` are both
written from `titanic.csv` by the lecture notebook, and could be deleted and regenerated at any time.
`titanic.csv` is the source, and nothing in this course writes over it.

---

## The World Bank country panel

`co2_emissions.csv` and `country_info.csv` are the two files that recur across the whole second half
of the course. They were downloaded from the [World Bank Open Data
API](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589) on **13 August 2026**, covering
**2000–2023**.

`co2_emissions.csv` has one row per entity per year, and these columns:

| Column | Indicator | World Bank code |
|---|---|---|
| `country` | entity name | |
| `code` | ISO 3166-1 alpha-3 code | |
| `year` | | |
| `co2_total` | CO₂ emissions, Mt CO₂e | `EN.GHG.CO2.MT.CE.AR5` |
| `population` | Population, total | `SP.POP.TOTL` |
| `urban` | Urban population, % of total | `SP.URB.TOTL.IN.ZS` |
| `gdp_pc` | GDP per capita, current US$ | `NY.GDP.PCAP.CD` |
| `electricity` | Access to electricity, % of population | `EG.ELC.ACCS.ZS` |
| `agriculture` | Agricultural land, % of land area | `AG.LND.AGRI.ZS` |
| `nat_resources` | Total natural resources rents, % of GDP | `NY.GDP.TOTL.RT.ZS` |
| `renew_energy` | Renewable energy consumption, % of final consumption | `EG.FEC.RNEW.ZS` |

`country_info.csv` has one row per entity: `name`, `code`, `region`, `incomeLevel`.

Three things about this data are worth knowing before you use it, and none of them are mistakes:

1. **It contains aggregates as well as countries.** 43 of the 260 entities are World Bank groupings
   such as `World`, `Arab World` or `East Asia & Pacific`. Adding them to a total counts the same
   emissions several times over. `country_info.csv` marks them with the region `Aggregates`.
2. **Values are missing, and not at random.** `population` and `urban` are complete;
   `nat_resources` is missing 759 times and `renew_energy` 635, mostly for small states and for the
   most recent years, because those series are published with a lag.
3. **Two entity names in `country_info.csv` carry a trailing space** — `"Sub-Saharan Africa "` and
   `"Latin America & Caribbean "` — exactly as the World Bank publishes them. Joining the two files on
   the name column therefore loses rows silently. Joining on `code` does not. This is what real data
   is like, and it is the reason to check a join rather than trust it.

Figures rounded for file size: emissions and rents to four decimals, shares to two or three, GDP per
capita to two. Population is exact.

World Bank data is published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
