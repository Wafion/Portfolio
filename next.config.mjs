/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  transpilePackages: ['three', '@react-three/fiber', '@react-three/drei'],
  webpack: (config, { dev }) => {
    if (dev) {
      // Prevent Windows pack cache ENOENT corruption in dev mode
      config.cache = {
        type: 'memory',
      };
    }
    return config;
  },
};

export default nextConfig;
