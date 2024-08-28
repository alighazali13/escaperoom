
module.exports = {
  content: ["../../templates/**/*.html"],
    theme: {
      extend: {
        fontFamily: {
          'YekanBakh-Light': ['YekanBakh-Light'],
          'YekanBakh-Regular': ['YekanBakh-Regular'],
          'YekanBakh-SemiBold': ['YekanBakh-SemiBold'],
          'YekanBakh-Bold': ['YekanBakh-Bold'],
          'YekanBakh-ExtraBold': ['YekanBakh-ExtraBold'],
          'YekanBakh-ExtraBlack': ['YekanBakh-ExtraBlack'],
          'DyeLine': ['DyeLine'],
        },
      },
      color: {
        'three': '#092635'
      }
    },
    daisyui: {
      themes: ["light"],
    },
    plugins: [
      require("daisyui"),
      require('@tailwindcss/forms'),
      require("@material-tailwind/html/utils/withMT")
    ]
    
  }