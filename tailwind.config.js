/** @type {import('tailwindcss').Config} */
export default {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  content: [],
  theme: {
    extend: {
      colors: {
        "gradient-1": "#6B21A8",
        "gradient-2": "#3b0764",
      },
    },
  },
  plugins: [],
}

