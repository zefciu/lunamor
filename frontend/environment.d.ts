declare global {
  namespace NodeJS {
    interface ProcessEnv {
      CLERK_PUBLIC_KEY: string;
    }
  }
}

export {};
