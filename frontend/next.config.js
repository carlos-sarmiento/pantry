/** @type {import('next').NextConfig} */
// const nextConfig =

module.exports = {
  experimental: {
    appDir: true,
  },
  async rewrites() {
    return [
      {
        source: '/graphql/:path*',
        destination: 'http://localhost:5121/graphql/:path*'
      }
    ]
  }
}
