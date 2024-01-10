<!-- DetailPage.svelte -->
<script>
  import { onMount } from "svelte";
  import { Line } from 'svelte-chartjs';
  import fastapi from "../../../lib/api";

  import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    LineElement,
    LinearScale,
    PointElement,
    CategoryScale,
  } from 'chart.js';

  ChartJS.register(
    Title,
    Tooltip,
    Legend,
    LineElement,
    LinearScale,
    PointElement,
    CategoryScale
  );

  export let params;

  let chartData = {};

  onMount(async () => {
    const device_uuid = params.device_uuid;

    try {
      const json = await new Promise((resolve, reject) => {
        fastapi('get', `/api/device/detail/${device_uuid}`, null, resolve, reject);
      });

      console.log("Received data:", json); // 데이터 출력

      if (json[0].records && json[0].records.length > 0) {
        const records = json[0].records;
        const labels = records.map(record => record.values._time);
        const values = records.map(record => record.values._value);

        chartData = {
          labels,
          datasets: [{
            label: 'Soil Humidity',
            data: values,
            fill: false,
            borderColor: 'rgba(75, 192, 192, 1)',
            tension: 0.1,
          }],
        };

        console.log("chartdata", chartData)
      }
    } catch (error) {
      console.error("Error fetching device details:", error);
    }
  });

  const chart_options = {
                scales: {
                    y : {
                        min: 0,
                        max: 100,
                    }
                }
            }
</script>

<h1>Device Details</h1>

{#if Object.keys(chartData).length > 0}
    <Line data={chartData} options={chart_options} />
{:else}
  <p>Loading...</p>
{/if}
