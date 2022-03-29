Currencies Analysis
================

***Analysis price of the my list of ~~the most promised cryptotokens~~
currencies.***

## Prepare

Install packages and set environment :earth\_asia:

`install.packages("azuremlsdk")`

``` r
suppressPackageStartupMessages({
  library(dplyr)
  library(tidyr)
  
  library(lubridate)
  library(stringr)
  
  library(gt)
  library(tidyverse)
  library(glue)
  
  library(ggplot2)
  
  library(azuremlsdk)
})
```

``` r
.azureml_dataset_name <- "Currencies"
```

Connect to Azure ML workspace:

``` r
ws <- azuremlsdk::load_workspace_from_config()
sprintf(
  "%s workspace located in %s region", ws$name, ws$location
)
```

    ## [1] "portf-opt-ws workspace located in westeurope region"

## Load dataset

``` r
currencies_ds <- azuremlsdk::get_dataset_by_name(ws, name = .azureml_dataset_name)
currencies_ds$name
```

    ## [1] "Currencies"

``` r
currencies_ds$description
```

    ## [1] "Source: https://www.kaggle.com/datasets/dhruvildave/currency-exchange-rates"

Get USD/RUB top higher rates:

``` r
quotes_df <- currencies_ds$to_pandas_dataframe()

# ~ 20 years, 150 currencies and 1.5M rows

quotes_df %>%
  filter(slug == "USD/RUB") %>%
  select(-slug) %>% 
  top_n(10) %>% 
  
  gt() %>%
  tab_header(
    title = "USD/RUB Rate",
    subtitle = glue("{min(quotes_df$date)} to {max(quotes_df$date)}")
  ) %>%
  fmt_date(
    columns = date,
    date_style = 6
  ) %>%
  fmt_number(
    columns = c(open, high, low, close)
  )
```

    ## Selecting by close

<div id="rzmyosotrn" style="overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>html {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
}

#rzmyosotrn .gt_table {
  display: table;
  border-collapse: collapse;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 16px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: auto;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #A8A8A8;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #A8A8A8;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
}

#rzmyosotrn .gt_heading {
  background-color: #FFFFFF;
  text-align: center;
  border-bottom-color: #FFFFFF;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#rzmyosotrn .gt_title {
  color: #333333;
  font-size: 125%;
  font-weight: initial;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-color: #FFFFFF;
  border-bottom-width: 0;
}

#rzmyosotrn .gt_subtitle {
  color: #333333;
  font-size: 85%;
  font-weight: initial;
  padding-top: 0;
  padding-bottom: 6px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-color: #FFFFFF;
  border-top-width: 0;
}

#rzmyosotrn .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#rzmyosotrn .gt_col_headings {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#rzmyosotrn .gt_col_heading {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 6px;
  padding-left: 5px;
  padding-right: 5px;
  overflow-x: hidden;
}

#rzmyosotrn .gt_column_spanner_outer {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  padding-top: 0;
  padding-bottom: 0;
  padding-left: 4px;
  padding-right: 4px;
}

#rzmyosotrn .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#rzmyosotrn .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#rzmyosotrn .gt_column_spanner {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 5px;
  overflow-x: hidden;
  display: inline-block;
  width: 100%;
}

#rzmyosotrn .gt_group_heading {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
}

#rzmyosotrn .gt_empty_group_heading {
  padding: 0.5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: middle;
}

#rzmyosotrn .gt_from_md > :first-child {
  margin-top: 0;
}

#rzmyosotrn .gt_from_md > :last-child {
  margin-bottom: 0;
}

#rzmyosotrn .gt_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  margin: 10px;
  border-top-style: solid;
  border-top-width: 1px;
  border-top-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  overflow-x: hidden;
}

#rzmyosotrn .gt_stub {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
}

#rzmyosotrn .gt_stub_row_group {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
  vertical-align: top;
}

#rzmyosotrn .gt_row_group_first td {
  border-top-width: 2px;
}

#rzmyosotrn .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#rzmyosotrn .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#rzmyosotrn .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#rzmyosotrn .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#rzmyosotrn .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#rzmyosotrn .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#rzmyosotrn .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#rzmyosotrn .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#rzmyosotrn .gt_footnotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#rzmyosotrn .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-left: 4px;
  padding-right: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#rzmyosotrn .gt_sourcenotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#rzmyosotrn .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#rzmyosotrn .gt_left {
  text-align: left;
}

#rzmyosotrn .gt_center {
  text-align: center;
}

#rzmyosotrn .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#rzmyosotrn .gt_font_normal {
  font-weight: normal;
}

#rzmyosotrn .gt_font_bold {
  font-weight: bold;
}

#rzmyosotrn .gt_font_italic {
  font-style: italic;
}

#rzmyosotrn .gt_super {
  font-size: 65%;
}

#rzmyosotrn .gt_footnote_marks {
  font-style: italic;
  font-weight: normal;
  font-size: 75%;
  vertical-align: 0.4em;
}

#rzmyosotrn .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#rzmyosotrn .gt_slash_mark {
  font-size: 0.7em;
  line-height: 0.7em;
  vertical-align: 0.15em;
}

#rzmyosotrn .gt_fraction_numerator {
  font-size: 0.6em;
  line-height: 0.6em;
  vertical-align: 0.45em;
}

#rzmyosotrn .gt_fraction_denominator {
  font-size: 0.6em;
  line-height: 0.6em;
  vertical-align: -0.05em;
}
</style>
<table class="gt_table">
  <thead class="gt_header">
    <tr>
      <th colspan="5" class="gt_heading gt_title gt_font_normal" style>USD/RUB Rate</th>
    </tr>
    <tr>
      <th colspan="5" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border" style>1996-10-30 to 2021-08-30</th>
    </tr>
  </thead>
  <thead class="gt_col_headings">
    <tr>
      <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1">date</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1">open</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1">high</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1">low</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1">close</th>
    </tr>
  </thead>
  <tbody class="gt_table_body">
    <tr><td class="gt_row gt_left">Jan 21, 2016</td>
<td class="gt_row gt_right">82.06</td>
<td class="gt_row gt_right">85.82</td>
<td class="gt_row gt_right">82.06</td>
<td class="gt_row gt_right">81.82</td></tr>
    <tr><td class="gt_row gt_left">Jan 22, 2016</td>
<td class="gt_row gt_right">80.61</td>
<td class="gt_row gt_right">81.26</td>
<td class="gt_row gt_right">77.94</td>
<td class="gt_row gt_right">82.90</td></tr>
    <tr><td class="gt_row gt_left">Jan 26, 2016</td>
<td class="gt_row gt_right">81.54</td>
<td class="gt_row gt_right">82.16</td>
<td class="gt_row gt_right">78.33</td>
<td class="gt_row gt_right">79.84</td></tr>
    <tr><td class="gt_row gt_left">Feb 3, 2016</td>
<td class="gt_row gt_right">79.56</td>
<td class="gt_row gt_right">79.75</td>
<td class="gt_row gt_right">77.87</td>
<td class="gt_row gt_right">79.71</td></tr>
    <tr><td class="gt_row gt_left">Feb 10, 2016</td>
<td class="gt_row gt_right">79.39</td>
<td class="gt_row gt_right">79.49</td>
<td class="gt_row gt_right">77.65</td>
<td class="gt_row gt_right">79.59</td></tr>
    <tr><td class="gt_row gt_left">Feb 12, 2016</td>
<td class="gt_row gt_right">79.36</td>
<td class="gt_row gt_right">79.74</td>
<td class="gt_row gt_right">78.59</td>
<td class="gt_row gt_right">79.77</td></tr>
    <tr><td class="gt_row gt_left">Mar 19, 2020</td>
<td class="gt_row gt_right">80.92</td>
<td class="gt_row gt_right">82.07</td>
<td class="gt_row gt_right">79.24</td>
<td class="gt_row gt_right">80.92</td></tr>
    <tr><td class="gt_row gt_left">Mar 23, 2020</td>
<td class="gt_row gt_right">79.72</td>
<td class="gt_row gt_right">81.34</td>
<td class="gt_row gt_right">79.49</td>
<td class="gt_row gt_right">79.84</td></tr>
    <tr><td class="gt_row gt_left">Mar 31, 2020</td>
<td class="gt_row gt_right">79.59</td>
<td class="gt_row gt_right">79.69</td>
<td class="gt_row gt_right">77.66</td>
<td class="gt_row gt_right">79.59</td></tr>
    <tr><td class="gt_row gt_left">Nov 3, 2020</td>
<td class="gt_row gt_right">80.55</td>
<td class="gt_row gt_right">80.57</td>
<td class="gt_row gt_right">79.05</td>
<td class="gt_row gt_right">80.52</td></tr>
  </tbody>
  
  
</table>
</div>

## Preprocessing data

Calculate `Return` and `Log Return` for last 10 years:

``` r
quotes_df %<>% 
  transmute(
    symbol = slug,
    price = close,
    date
  ) %>% 
  
  filter(
    str_detect(symbol, "USD/") &
    date > max(date) - lubridate::years(10)
  ) %>% 
  
  filter(!(symbol == "USD/RUB" & price < 1)) %>% 
  
  arrange(date) %>% 
  group_by(symbol) %>%
  
  mutate(
    return = c(NA_real_, diff(price))/lag(price),
    log_return = log(1 + return)
  ) %>% 
  na.omit
```

Base and quote currencies:

``` r
quotes_stats <- quotes_df %>% 

  summarise(
    max_price = max(price), 
    min_price = min(price),
    last_price = last(price),
    max_min_rate = max(price)/min(price),
    volatility = sd(log_return)
  )

volatility_threshold <- quotes_stats %>% pull(volatility) %>% quantile(probs = .75)


quotes_stats %>% 
  filter(
    volatility <= volatility_threshold | 
    symbol == "USD/RUB"
  ) %>% 
  mutate(
    `100x Volatility` = volatility*100
  ) %>% 
  arrange(volatility) %>% 
  select(-volatility) %>% 
  
  gt() %>% 
  tab_header(
    title = "The Least Volatile Currencies",
    subtitle = glue("{min(quotes_df$date)} to {max(quotes_df$date)}")
  ) %>%
  fmt_number(
    columns = c(max_price, min_price, max_min_rate, `100x Volatility`)
  )
```

<div id="kerqnzolxy" style="overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>html {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
}

#kerqnzolxy .gt_table {
  display: table;
  border-collapse: collapse;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 16px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: auto;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #A8A8A8;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #A8A8A8;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
}

#kerqnzolxy .gt_heading {
  background-color: #FFFFFF;
  text-align: center;
  border-bottom-color: #FFFFFF;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#kerqnzolxy .gt_title {
  color: #333333;
  font-size: 125%;
  font-weight: initial;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-color: #FFFFFF;
  border-bottom-width: 0;
}

#kerqnzolxy .gt_subtitle {
  color: #333333;
  font-size: 85%;
  font-weight: initial;
  padding-top: 0;
  padding-bottom: 6px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-color: #FFFFFF;
  border-top-width: 0;
}

#kerqnzolxy .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#kerqnzolxy .gt_col_headings {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#kerqnzolxy .gt_col_heading {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 6px;
  padding-left: 5px;
  padding-right: 5px;
  overflow-x: hidden;
}

#kerqnzolxy .gt_column_spanner_outer {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  padding-top: 0;
  padding-bottom: 0;
  padding-left: 4px;
  padding-right: 4px;
}

#kerqnzolxy .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#kerqnzolxy .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#kerqnzolxy .gt_column_spanner {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 5px;
  overflow-x: hidden;
  display: inline-block;
  width: 100%;
}

#kerqnzolxy .gt_group_heading {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
}

#kerqnzolxy .gt_empty_group_heading {
  padding: 0.5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: middle;
}

#kerqnzolxy .gt_from_md > :first-child {
  margin-top: 0;
}

#kerqnzolxy .gt_from_md > :last-child {
  margin-bottom: 0;
}

#kerqnzolxy .gt_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  margin: 10px;
  border-top-style: solid;
  border-top-width: 1px;
  border-top-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  overflow-x: hidden;
}

#kerqnzolxy .gt_stub {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
}

#kerqnzolxy .gt_stub_row_group {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
  vertical-align: top;
}

#kerqnzolxy .gt_row_group_first td {
  border-top-width: 2px;
}

#kerqnzolxy .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#kerqnzolxy .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#kerqnzolxy .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#kerqnzolxy .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#kerqnzolxy .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#kerqnzolxy .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#kerqnzolxy .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#kerqnzolxy .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#kerqnzolxy .gt_footnotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#kerqnzolxy .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-left: 4px;
  padding-right: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#kerqnzolxy .gt_sourcenotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#kerqnzolxy .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#kerqnzolxy .gt_left {
  text-align: left;
}

#kerqnzolxy .gt_center {
  text-align: center;
}

#kerqnzolxy .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#kerqnzolxy .gt_font_normal {
  font-weight: normal;
}

#kerqnzolxy .gt_font_bold {
  font-weight: bold;
}

#kerqnzolxy .gt_font_italic {
  font-style: italic;
}

#kerqnzolxy .gt_super {
  font-size: 65%;
}

#kerqnzolxy .gt_footnote_marks {
  font-style: italic;
  font-weight: normal;
  font-size: 75%;
  vertical-align: 0.4em;
}

#kerqnzolxy .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#kerqnzolxy .gt_slash_mark {
  font-size: 0.7em;
  line-height: 0.7em;
  vertical-align: 0.15em;
}

#kerqnzolxy .gt_fraction_numerator {
  font-size: 0.6em;
  line-height: 0.6em;
  vertical-align: 0.45em;
}

#kerqnzolxy .gt_fraction_denominator {
  font-size: 0.6em;
  line-height: 0.6em;
  vertical-align: -0.05em;
}
</style>
<table class="gt_table">
  <thead class="gt_header">
    <tr>
      <th colspan="6" class="gt_heading gt_title gt_font_normal" style>The Least Volatile Currencies</th>
    </tr>
    <tr>
      <th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border" style>2011-09-01 to 2021-08-30</th>
    </tr>
  </thead>
  <thead class="gt_col_headings">
    <tr>
      <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1">symbol</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1">max_price</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1">min_price</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1">last_price</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1">max_min_rate</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1">100x Volatility</th>
    </tr>
  </thead>
  <tbody class="gt_table_body">
    <tr><td class="gt_row gt_left">USD/AED</td>
<td class="gt_row gt_right">3.67</td>
<td class="gt_row gt_right">3.67</td>
<td class="gt_row gt_right">3.67280</td>
<td class="gt_row gt_right">1.00</td>
<td class="gt_row gt_right">0.01</td></tr>
    <tr><td class="gt_row gt_left">USD/HKD</td>
<td class="gt_row gt_right">7.85</td>
<td class="gt_row gt_right">7.75</td>
<td class="gt_row gt_right">7.78694</td>
<td class="gt_row gt_right">1.01</td>
<td class="gt_row gt_right">0.03</td></tr>
    <tr><td class="gt_row gt_left">USD/KWD</td>
<td class="gt_row gt_right">0.31</td>
<td class="gt_row gt_right">0.27</td>
<td class="gt_row gt_right">0.30060</td>
<td class="gt_row gt_right">1.16</td>
<td class="gt_row gt_right">0.16</td></tr>
    <tr><td class="gt_row gt_left">USD/CNY</td>
<td class="gt_row gt_right">7.18</td>
<td class="gt_row gt_right">6.03</td>
<td class="gt_row gt_right">6.46580</td>
<td class="gt_row gt_right">1.19</td>
<td class="gt_row gt_right">0.23</td></tr>
    <tr><td class="gt_row gt_left">USD/DJF</td>
<td class="gt_row gt_right">177.72</td>
<td class="gt_row gt_right">172.00</td>
<td class="gt_row gt_right">177.50000</td>
<td class="gt_row gt_right">1.03</td>
<td class="gt_row gt_right">0.28</td></tr>
    <tr><td class="gt_row gt_left">USD/SGD</td>
<td class="gt_row gt_right">1.46</td>
<td class="gt_row gt_right">1.20</td>
<td class="gt_row gt_right">1.34448</td>
<td class="gt_row gt_right">1.21</td>
<td class="gt_row gt_right">0.33</td></tr>
    <tr><td class="gt_row gt_left">USD/SAR</td>
<td class="gt_row gt_right">3.77</td>
<td class="gt_row gt_right">3.30</td>
<td class="gt_row gt_right">3.75050</td>
<td class="gt_row gt_right">1.14</td>
<td class="gt_row gt_right">0.39</td></tr>
    <tr><td class="gt_row gt_left">USD/GTQ</td>
<td class="gt_row gt_right">7.89</td>
<td class="gt_row gt_right">7.04</td>
<td class="gt_row gt_right">7.72750</td>
<td class="gt_row gt_right">1.12</td>
<td class="gt_row gt_right">0.41</td></tr>
    <tr><td class="gt_row gt_left">USD/ILS</td>
<td class="gt_row gt_right">4.07</td>
<td class="gt_row gt_right">3.13</td>
<td class="gt_row gt_right">3.20490</td>
<td class="gt_row gt_right">1.30</td>
<td class="gt_row gt_right">0.45</td></tr>
    <tr><td class="gt_row gt_left">USD/TTD</td>
<td class="gt_row gt_right">6.78</td>
<td class="gt_row gt_right">5.93</td>
<td class="gt_row gt_right">6.76320</td>
<td class="gt_row gt_right">1.14</td>
<td class="gt_row gt_right">0.47</td></tr>
    <tr><td class="gt_row gt_left">USD/CAD</td>
<td class="gt_row gt_right">1.46</td>
<td class="gt_row gt_right">0.97</td>
<td class="gt_row gt_right">1.26050</td>
<td class="gt_row gt_right">1.51</td>
<td class="gt_row gt_right">0.47</td></tr>
    <tr><td class="gt_row gt_left">USD/MYR</td>
<td class="gt_row gt_right">4.49</td>
<td class="gt_row gt_right">2.96</td>
<td class="gt_row gt_right">4.15500</td>
<td class="gt_row gt_right">1.52</td>
<td class="gt_row gt_right">0.50</td></tr>
    <tr><td class="gt_row gt_left">USD/DKK</td>
<td class="gt_row gt_right">7.15</td>
<td class="gt_row gt_right">5.18</td>
<td class="gt_row gt_right">6.29986</td>
<td class="gt_row gt_right">1.38</td>
<td class="gt_row gt_right">0.51</td></tr>
    <tr><td class="gt_row gt_left">USD/EUR</td>
<td class="gt_row gt_right">0.96</td>
<td class="gt_row gt_right">0.70</td>
<td class="gt_row gt_right">0.84700</td>
<td class="gt_row gt_right">1.38</td>
<td class="gt_row gt_right">0.51</td></tr>
    <tr><td class="gt_row gt_left">USD/CRC</td>
<td class="gt_row gt_right">619.70</td>
<td class="gt_row gt_right">478.54</td>
<td class="gt_row gt_right">619.70001</td>
<td class="gt_row gt_right">1.29</td>
<td class="gt_row gt_right">0.53</td></tr>
    <tr><td class="gt_row gt_left">USD/PHP</td>
<td class="gt_row gt_right">54.23</td>
<td class="gt_row gt_right">39.75</td>
<td class="gt_row gt_right">49.70500</td>
<td class="gt_row gt_right">1.36</td>
<td class="gt_row gt_right">0.54</td></tr>
    <tr><td class="gt_row gt_left">USD/INR</td>
<td class="gt_row gt_right">77.57</td>
<td class="gt_row gt_right">45.70</td>
<td class="gt_row gt_right">73.29200</td>
<td class="gt_row gt_right">1.70</td>
<td class="gt_row gt_right">0.54</td></tr>
    <tr><td class="gt_row gt_left">USD/RON</td>
<td class="gt_row gt_right">4.54</td>
<td class="gt_row gt_right">2.93</td>
<td class="gt_row gt_right">4.17920</td>
<td class="gt_row gt_right">1.55</td>
<td class="gt_row gt_right">0.55</td></tr>
    <tr><td class="gt_row gt_left">USD/JPY</td>
<td class="gt_row gt_right">125.63</td>
<td class="gt_row gt_right">75.74</td>
<td class="gt_row gt_right">109.90200</td>
<td class="gt_row gt_right">1.66</td>
<td class="gt_row gt_right">0.55</td></tr>
    <tr><td class="gt_row gt_left">USD/GBP</td>
<td class="gt_row gt_right">0.87</td>
<td class="gt_row gt_right">0.58</td>
<td class="gt_row gt_right">0.72661</td>
<td class="gt_row gt_right">1.49</td>
<td class="gt_row gt_right">0.55</td></tr>
    <tr><td class="gt_row gt_left">USD/JMD</td>
<td class="gt_row gt_right">153.88</td>
<td class="gt_row gt_right">83.37</td>
<td class="gt_row gt_right">150.53000</td>
<td class="gt_row gt_right">1.85</td>
<td class="gt_row gt_right">0.56</td></tr>
    <tr><td class="gt_row gt_left">USD/MKD</td>
<td class="gt_row gt_right">58.92</td>
<td class="gt_row gt_right">42.07</td>
<td class="gt_row gt_right">51.98000</td>
<td class="gt_row gt_right">1.40</td>
<td class="gt_row gt_right">0.58</td></tr>
    <tr><td class="gt_row gt_left">USD/MDL</td>
<td class="gt_row gt_right">20.31</td>
<td class="gt_row gt_right">11.09</td>
<td class="gt_row gt_right">17.58000</td>
<td class="gt_row gt_right">1.83</td>
<td class="gt_row gt_right">0.61</td></tr>
    <tr><td class="gt_row gt_left">USD/BDT</td>
<td class="gt_row gt_right">84.72</td>
<td class="gt_row gt_right">72.39</td>
<td class="gt_row gt_right">84.72000</td>
<td class="gt_row gt_right">1.17</td>
<td class="gt_row gt_right">0.62</td></tr>
    <tr><td class="gt_row gt_left">USD/AUD</td>
<td class="gt_row gt_right">1.74</td>
<td class="gt_row gt_right">0.93</td>
<td class="gt_row gt_right">1.36995</td>
<td class="gt_row gt_right">1.88</td>
<td class="gt_row gt_right">0.63</td></tr>
    <tr><td class="gt_row gt_left">USD/SEK</td>
<td class="gt_row gt_right">10.44</td>
<td class="gt_row gt_right">6.29</td>
<td class="gt_row gt_right">8.61840</td>
<td class="gt_row gt_right">1.66</td>
<td class="gt_row gt_right">0.64</td></tr>
    <tr><td class="gt_row gt_left">USD/CHF</td>
<td class="gt_row gt_right">1.03</td>
<td class="gt_row gt_right">0.79</td>
<td class="gt_row gt_right">0.91691</td>
<td class="gt_row gt_right">1.31</td>
<td class="gt_row gt_right">0.64</td></tr>
    <tr><td class="gt_row gt_left">USD/CZK</td>
<td class="gt_row gt_right">26.03</td>
<td class="gt_row gt_right">16.75</td>
<td class="gt_row gt_right">21.67120</td>
<td class="gt_row gt_right">1.55</td>
<td class="gt_row gt_right">0.64</td></tr>
    <tr><td class="gt_row gt_left">USD/BWP</td>
<td class="gt_row gt_right">12.19</td>
<td class="gt_row gt_right">6.58</td>
<td class="gt_row gt_right">11.11850</td>
<td class="gt_row gt_right">1.85</td>
<td class="gt_row gt_right">0.66</td></tr>
    <tr><td class="gt_row gt_left">USD/NZD</td>
<td class="gt_row gt_right">1.78</td>
<td class="gt_row gt_right">1.13</td>
<td class="gt_row gt_right">1.42710</td>
<td class="gt_row gt_right">1.57</td>
<td class="gt_row gt_right">0.66</td></tr>
    <tr><td class="gt_row gt_left">USD/THB</td>
<td class="gt_row gt_right">36.43</td>
<td class="gt_row gt_right">28.07</td>
<td class="gt_row gt_right">32.44700</td>
<td class="gt_row gt_right">1.30</td>
<td class="gt_row gt_right">0.67</td></tr>
    <tr><td class="gt_row gt_left">USD/LKR</td>
<td class="gt_row gt_right">199.43</td>
<td class="gt_row gt_right">106.22</td>
<td class="gt_row gt_right">199.42999</td>
<td class="gt_row gt_right">1.88</td>
<td class="gt_row gt_right">0.67</td></tr>
    <tr><td class="gt_row gt_left">USD/KRW</td>
<td class="gt_row gt_right">1,262.93</td>
<td class="gt_row gt_right">999.83</td>
<td class="gt_row gt_right">1165.89001</td>
<td class="gt_row gt_right">1.26</td>
<td class="gt_row gt_right">0.70</td></tr>
    <tr><td class="gt_row gt_left">USD/RSD</td>
<td class="gt_row gt_right">118.47</td>
<td class="gt_row gt_right">70.05</td>
<td class="gt_row gt_right">99.28820</td>
<td class="gt_row gt_right">1.69</td>
<td class="gt_row gt_right">0.70</td></tr>
    <tr><td class="gt_row gt_left">USD/UYU</td>
<td class="gt_row gt_right">45.31</td>
<td class="gt_row gt_right">18.08</td>
<td class="gt_row gt_right">42.53000</td>
<td class="gt_row gt_right">2.51</td>
<td class="gt_row gt_right">0.71</td></tr>
    <tr><td class="gt_row gt_left">USD/PLN</td>
<td class="gt_row gt_right">4.28</td>
<td class="gt_row gt_right">2.87</td>
<td class="gt_row gt_right">3.86140</td>
<td class="gt_row gt_right">1.49</td>
<td class="gt_row gt_right">0.72</td></tr>
    <tr><td class="gt_row gt_left">USD/HUF</td>
<td class="gt_row gt_right">338.26</td>
<td class="gt_row gt_right">188.61</td>
<td class="gt_row gt_right">294.66000</td>
<td class="gt_row gt_right">1.79</td>
<td class="gt_row gt_right">0.74</td></tr>
    <tr><td class="gt_row gt_left">USD/MUR</td>
<td class="gt_row gt_right">42.55</td>
<td class="gt_row gt_right">26.50</td>
<td class="gt_row gt_right">42.55000</td>
<td class="gt_row gt_right">1.61</td>
<td class="gt_row gt_right">0.79</td></tr>
    <tr><td class="gt_row gt_left">USD/MXN</td>
<td class="gt_row gt_right">25.34</td>
<td class="gt_row gt_right">11.98</td>
<td class="gt_row gt_right">20.13500</td>
<td class="gt_row gt_right">2.11</td>
<td class="gt_row gt_right">0.80</td></tr>
    <tr><td class="gt_row gt_left">USD/NIO</td>
<td class="gt_row gt_right">35.13</td>
<td class="gt_row gt_right">22.05</td>
<td class="gt_row gt_right">35.00000</td>
<td class="gt_row gt_right">1.59</td>
<td class="gt_row gt_right">0.84</td></tr>
    <tr><td class="gt_row gt_left">USD/KZT</td>
<td class="gt_row gt_right">454.34</td>
<td class="gt_row gt_right">174.15</td>
<td class="gt_row gt_right">427.17999</td>
<td class="gt_row gt_right">2.61</td>
<td class="gt_row gt_right">0.84</td></tr>
    <tr><td class="gt_row gt_left">USD/QAR</td>
<td class="gt_row gt_right">3.90</td>
<td class="gt_row gt_right">3.00</td>
<td class="gt_row gt_right">3.64000</td>
<td class="gt_row gt_right">1.30</td>
<td class="gt_row gt_right">0.95</td></tr>
    <tr><td class="gt_row gt_left">USD/TRY</td>
<td class="gt_row gt_right">8.78</td>
<td class="gt_row gt_right">1.71</td>
<td class="gt_row gt_right">8.37690</td>
<td class="gt_row gt_right">5.12</td>
<td class="gt_row gt_right">0.97</td></tr>
    <tr><td class="gt_row gt_left">USD/ZAR</td>
<td class="gt_row gt_right">19.25</td>
<td class="gt_row gt_right">6.98</td>
<td class="gt_row gt_right">14.66110</td>
<td class="gt_row gt_right">2.76</td>
<td class="gt_row gt_right">0.99</td></tr>
    <tr><td class="gt_row gt_left">USD/RUB</td>
<td class="gt_row gt_right">82.90</td>
<td class="gt_row gt_right">28.79</td>
<td class="gt_row gt_right">73.50400</td>
<td class="gt_row gt_right">2.88</td>
<td class="gt_row gt_right">1.05</td></tr>
    <tr><td class="gt_row gt_left">USD/ZMW</td>
<td class="gt_row gt_right">22.64</td>
<td class="gt_row gt_right">5.11</td>
<td class="gt_row gt_right">15.82000</td>
<td class="gt_row gt_right">4.43</td>
<td class="gt_row gt_right">1.06</td></tr>
    <tr><td class="gt_row gt_left">USD/BRL</td>
<td class="gt_row gt_right">5.89</td>
<td class="gt_row gt_right">1.58</td>
<td class="gt_row gt_right">5.19380</td>
<td class="gt_row gt_right">3.72</td>
<td class="gt_row gt_right">1.08</td></tr>
    <tr><td class="gt_row gt_left">USD/ARS</td>
<td class="gt_row gt_right">97.70</td>
<td class="gt_row gt_right">4.10</td>
<td class="gt_row gt_right">97.70000</td>
<td class="gt_row gt_right">23.85</td>
<td class="gt_row gt_right">1.11</td></tr>
    <tr><td class="gt_row gt_left">USD/TND</td>
<td class="gt_row gt_right">3.06</td>
<td class="gt_row gt_right">1.37</td>
<td class="gt_row gt_right">2.79000</td>
<td class="gt_row gt_right">2.23</td>
<td class="gt_row gt_right">1.17</td></tr>
    <tr><td class="gt_row gt_left">USD/BGN</td>
<td class="gt_row gt_right">1.87</td>
<td class="gt_row gt_right">1.21</td>
<td class="gt_row gt_right">1.65734</td>
<td class="gt_row gt_right">1.55</td>
<td class="gt_row gt_right">1.28</td></tr>
    <tr><td class="gt_row gt_left">USD/EGP</td>
<td class="gt_row gt_right">19.60</td>
<td class="gt_row gt_right">5.83</td>
<td class="gt_row gt_right">15.65000</td>
<td class="gt_row gt_right">3.37</td>
<td class="gt_row gt_right">1.29</td></tr>
    <tr><td class="gt_row gt_left">USD/NOK</td>
<td class="gt_row gt_right">11.76</td>
<td class="gt_row gt_right">5.36</td>
<td class="gt_row gt_right">8.66435</td>
<td class="gt_row gt_right">2.19</td>
<td class="gt_row gt_right">1.31</td></tr>
    <tr><td class="gt_row gt_left">USD/PEN</td>
<td class="gt_row gt_right">4.11</td>
<td class="gt_row gt_right">2.38</td>
<td class="gt_row gt_right">4.06940</td>
<td class="gt_row gt_right">1.72</td>
<td class="gt_row gt_right">1.34</td></tr>
    <tr><td class="gt_row gt_left">USD/BYN</td>
<td class="gt_row gt_right">3.08</td>
<td class="gt_row gt_right">0.51</td>
<td class="gt_row gt_right">2.51000</td>
<td class="gt_row gt_right">6.04</td>
<td class="gt_row gt_right">1.37</td></tr>
    <tr><td class="gt_row gt_left">USD/MAD</td>
<td class="gt_row gt_right">10.29</td>
<td class="gt_row gt_right">7.89</td>
<td class="gt_row gt_right">8.95300</td>
<td class="gt_row gt_right">1.30</td>
<td class="gt_row gt_right">1.43</td></tr>
    <tr><td class="gt_row gt_left">USD/UAH</td>
<td class="gt_row gt_right">33.50</td>
<td class="gt_row gt_right">7.80</td>
<td class="gt_row gt_right">26.92000</td>
<td class="gt_row gt_right">4.30</td>
<td class="gt_row gt_right">1.83</td></tr>
    <tr><td class="gt_row gt_left">USD/SDG</td>
<td class="gt_row gt_right">451.00</td>
<td class="gt_row gt_right">1.39</td>
<td class="gt_row gt_right">440.03491</td>
<td class="gt_row gt_right">324.46</td>
<td class="gt_row gt_right">5.96</td></tr>
    <tr><td class="gt_row gt_left">USD/BND</td>
<td class="gt_row gt_right">1.43</td>
<td class="gt_row gt_right">0.66</td>
<td class="gt_row gt_right">1.34470</td>
<td class="gt_row gt_right">2.18</td>
<td class="gt_row gt_right">6.29</td></tr>
    <tr><td class="gt_row gt_left">USD/XOF</td>
<td class="gt_row gt_right">647.00</td>
<td class="gt_row gt_right">58.00</td>
<td class="gt_row gt_right">555.46997</td>
<td class="gt_row gt_right">11.16</td>
<td class="gt_row gt_right">6.44</td></tr>
    <tr><td class="gt_row gt_left">USD/IDR</td>
<td class="gt_row gt_right">16,504.80</td>
<td class="gt_row gt_right">892.00</td>
<td class="gt_row gt_right">14370.00000</td>
<td class="gt_row gt_right">18.50</td>
<td class="gt_row gt_right">6.58</td></tr>
    <tr><td class="gt_row gt_left">USD/HNL</td>
<td class="gt_row gt_right">24.90</td>
<td class="gt_row gt_right">3.00</td>
<td class="gt_row gt_right">23.82560</td>
<td class="gt_row gt_right">8.30</td>
<td class="gt_row gt_right">8.14</td></tr>
  </tbody>
  
  
</table>
</div>

My broker available pairs:

``` r
symbols  <- c(
  'RUB', 
  'EUR', 'GBP', 'CHF', 'CNY', 'HKD', 'JPY', 'SEK', 'SGD', 'AUD',  
  'AED', 'KZT', 'BYN', 'TRY', 'MXN'
)

quotes_stats %>% 
  filter(
    symbol %in% str_c("USD", symbols, sep = "/")
  ) %>% 
  mutate(
    `100x Volatility` = volatility*100
  ) %>% 
  arrange(volatility) %>% 
  select(-volatility) %>% 
  
  gt() %>% 
  tab_header(
    title = "The Most Promised Currencies",
    subtitle = glue("{min(quotes_df$date)} to {max(quotes_df$date)}")
  ) %>%
  fmt_number(
    columns = c(max_price, min_price, max_min_rate, `100x Volatility`)
  )
```

<div id="fqnemuoohg" style="overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>html {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
}

#fqnemuoohg .gt_table {
  display: table;
  border-collapse: collapse;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 16px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: auto;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #A8A8A8;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #A8A8A8;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
}

#fqnemuoohg .gt_heading {
  background-color: #FFFFFF;
  text-align: center;
  border-bottom-color: #FFFFFF;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#fqnemuoohg .gt_title {
  color: #333333;
  font-size: 125%;
  font-weight: initial;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-color: #FFFFFF;
  border-bottom-width: 0;
}

#fqnemuoohg .gt_subtitle {
  color: #333333;
  font-size: 85%;
  font-weight: initial;
  padding-top: 0;
  padding-bottom: 6px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-color: #FFFFFF;
  border-top-width: 0;
}

#fqnemuoohg .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#fqnemuoohg .gt_col_headings {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}

#fqnemuoohg .gt_col_heading {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 6px;
  padding-left: 5px;
  padding-right: 5px;
  overflow-x: hidden;
}

#fqnemuoohg .gt_column_spanner_outer {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  padding-top: 0;
  padding-bottom: 0;
  padding-left: 4px;
  padding-right: 4px;
}

#fqnemuoohg .gt_column_spanner_outer:first-child {
  padding-left: 0;
}

#fqnemuoohg .gt_column_spanner_outer:last-child {
  padding-right: 0;
}

#fqnemuoohg .gt_column_spanner {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 5px;
  overflow-x: hidden;
  display: inline-block;
  width: 100%;
}

#fqnemuoohg .gt_group_heading {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
}

#fqnemuoohg .gt_empty_group_heading {
  padding: 0.5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: middle;
}

#fqnemuoohg .gt_from_md > :first-child {
  margin-top: 0;
}

#fqnemuoohg .gt_from_md > :last-child {
  margin-bottom: 0;
}

#fqnemuoohg .gt_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  margin: 10px;
  border-top-style: solid;
  border-top-width: 1px;
  border-top-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  overflow-x: hidden;
}

#fqnemuoohg .gt_stub {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
}

#fqnemuoohg .gt_stub_row_group {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
  vertical-align: top;
}

#fqnemuoohg .gt_row_group_first td {
  border-top-width: 2px;
}

#fqnemuoohg .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#fqnemuoohg .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}

#fqnemuoohg .gt_first_summary_row.thick {
  border-top-width: 2px;
}

#fqnemuoohg .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#fqnemuoohg .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}

#fqnemuoohg .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}

#fqnemuoohg .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}

#fqnemuoohg .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}

#fqnemuoohg .gt_footnotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#fqnemuoohg .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-left: 4px;
  padding-right: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#fqnemuoohg .gt_sourcenotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}

#fqnemuoohg .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}

#fqnemuoohg .gt_left {
  text-align: left;
}

#fqnemuoohg .gt_center {
  text-align: center;
}

#fqnemuoohg .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

#fqnemuoohg .gt_font_normal {
  font-weight: normal;
}

#fqnemuoohg .gt_font_bold {
  font-weight: bold;
}

#fqnemuoohg .gt_font_italic {
  font-style: italic;
}

#fqnemuoohg .gt_super {
  font-size: 65%;
}

#fqnemuoohg .gt_footnote_marks {
  font-style: italic;
  font-weight: normal;
  font-size: 75%;
  vertical-align: 0.4em;
}

#fqnemuoohg .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}

#fqnemuoohg .gt_slash_mark {
  font-size: 0.7em;
  line-height: 0.7em;
  vertical-align: 0.15em;
}

#fqnemuoohg .gt_fraction_numerator {
  font-size: 0.6em;
  line-height: 0.6em;
  vertical-align: 0.45em;
}

#fqnemuoohg .gt_fraction_denominator {
  font-size: 0.6em;
  line-height: 0.6em;
  vertical-align: -0.05em;
}
</style>
<table class="gt_table">
  <thead class="gt_header">
    <tr>
      <th colspan="6" class="gt_heading gt_title gt_font_normal" style>The Most Promised Currencies</th>
    </tr>
    <tr>
      <th colspan="6" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border" style>2011-09-01 to 2021-08-30</th>
    </tr>
  </thead>
  <thead class="gt_col_headings">
    <tr>
      <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1">symbol</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1">max_price</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1">min_price</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1">last_price</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1">max_min_rate</th>
      <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1">100x Volatility</th>
    </tr>
  </thead>
  <tbody class="gt_table_body">
    <tr><td class="gt_row gt_left">USD/AED</td>
<td class="gt_row gt_right">3.67</td>
<td class="gt_row gt_right">3.67</td>
<td class="gt_row gt_right">3.67280</td>
<td class="gt_row gt_right">1.00</td>
<td class="gt_row gt_right">0.01</td></tr>
    <tr><td class="gt_row gt_left">USD/HKD</td>
<td class="gt_row gt_right">7.85</td>
<td class="gt_row gt_right">7.75</td>
<td class="gt_row gt_right">7.78694</td>
<td class="gt_row gt_right">1.01</td>
<td class="gt_row gt_right">0.03</td></tr>
    <tr><td class="gt_row gt_left">USD/CNY</td>
<td class="gt_row gt_right">7.18</td>
<td class="gt_row gt_right">6.03</td>
<td class="gt_row gt_right">6.46580</td>
<td class="gt_row gt_right">1.19</td>
<td class="gt_row gt_right">0.23</td></tr>
    <tr><td class="gt_row gt_left">USD/SGD</td>
<td class="gt_row gt_right">1.46</td>
<td class="gt_row gt_right">1.20</td>
<td class="gt_row gt_right">1.34448</td>
<td class="gt_row gt_right">1.21</td>
<td class="gt_row gt_right">0.33</td></tr>
    <tr><td class="gt_row gt_left">USD/EUR</td>
<td class="gt_row gt_right">0.96</td>
<td class="gt_row gt_right">0.70</td>
<td class="gt_row gt_right">0.84700</td>
<td class="gt_row gt_right">1.38</td>
<td class="gt_row gt_right">0.51</td></tr>
    <tr><td class="gt_row gt_left">USD/JPY</td>
<td class="gt_row gt_right">125.63</td>
<td class="gt_row gt_right">75.74</td>
<td class="gt_row gt_right">109.90200</td>
<td class="gt_row gt_right">1.66</td>
<td class="gt_row gt_right">0.55</td></tr>
    <tr><td class="gt_row gt_left">USD/GBP</td>
<td class="gt_row gt_right">0.87</td>
<td class="gt_row gt_right">0.58</td>
<td class="gt_row gt_right">0.72661</td>
<td class="gt_row gt_right">1.49</td>
<td class="gt_row gt_right">0.55</td></tr>
    <tr><td class="gt_row gt_left">USD/AUD</td>
<td class="gt_row gt_right">1.74</td>
<td class="gt_row gt_right">0.93</td>
<td class="gt_row gt_right">1.36995</td>
<td class="gt_row gt_right">1.88</td>
<td class="gt_row gt_right">0.63</td></tr>
    <tr><td class="gt_row gt_left">USD/SEK</td>
<td class="gt_row gt_right">10.44</td>
<td class="gt_row gt_right">6.29</td>
<td class="gt_row gt_right">8.61840</td>
<td class="gt_row gt_right">1.66</td>
<td class="gt_row gt_right">0.64</td></tr>
    <tr><td class="gt_row gt_left">USD/CHF</td>
<td class="gt_row gt_right">1.03</td>
<td class="gt_row gt_right">0.79</td>
<td class="gt_row gt_right">0.91691</td>
<td class="gt_row gt_right">1.31</td>
<td class="gt_row gt_right">0.64</td></tr>
    <tr><td class="gt_row gt_left">USD/MXN</td>
<td class="gt_row gt_right">25.34</td>
<td class="gt_row gt_right">11.98</td>
<td class="gt_row gt_right">20.13500</td>
<td class="gt_row gt_right">2.11</td>
<td class="gt_row gt_right">0.80</td></tr>
    <tr><td class="gt_row gt_left">USD/KZT</td>
<td class="gt_row gt_right">454.34</td>
<td class="gt_row gt_right">174.15</td>
<td class="gt_row gt_right">427.17999</td>
<td class="gt_row gt_right">2.61</td>
<td class="gt_row gt_right">0.84</td></tr>
    <tr><td class="gt_row gt_left">USD/TRY</td>
<td class="gt_row gt_right">8.78</td>
<td class="gt_row gt_right">1.71</td>
<td class="gt_row gt_right">8.37690</td>
<td class="gt_row gt_right">5.12</td>
<td class="gt_row gt_right">0.97</td></tr>
    <tr><td class="gt_row gt_left">USD/RUB</td>
<td class="gt_row gt_right">82.90</td>
<td class="gt_row gt_right">28.79</td>
<td class="gt_row gt_right">73.50400</td>
<td class="gt_row gt_right">2.88</td>
<td class="gt_row gt_right">1.05</td></tr>
    <tr><td class="gt_row gt_left">USD/BYN</td>
<td class="gt_row gt_right">3.08</td>
<td class="gt_row gt_right">0.51</td>
<td class="gt_row gt_right">2.51000</td>
<td class="gt_row gt_right">6.04</td>
<td class="gt_row gt_right">1.37</td></tr>
  </tbody>
  
  
</table>
</div>

Plot exchange rate for out favorites:

Define low risk symbols:

``` r
low_risk_symbols <- quotes_stats %>% 
  filter(
    symbol %in% str_c("USD", symbols, sep = "/")
  ) %>% 
  filter(
    volatility <= volatility_threshold | 
    symbol == "USD/RUB"
  ) %>% 
  pull(symbol) %>% 
  unique

cat(
  sprintf(
    "['%s']",
    paste(low_risk_symbols, collapse = "', '")
))
```

    ## ['USD/AED', 'USD/AUD', 'USD/BYN', 'USD/CHF', 'USD/CNY', 'USD/EUR', 'USD/GBP', 'USD/HKD', 'USD/JPY', 'USD/KZT', 'USD/MXN', 'USD/RUB', 'USD/SEK', 'USD/SGD', 'USD/TRY']
