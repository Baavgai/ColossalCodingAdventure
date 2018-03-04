import { GameDef } from './cca-lib';
export interface DisplayManagerConfig {
    eleId?: string;
    width?: number;
    height?: number;
    entryPrompt?: string;
    noKeyBind?: boolean;
    sendLines?: (lines: string[]) => void;
    notifyInput?: (msg: string, display: DisplayManager) => void;
}
export declare class DisplayManager {
    private width;
    private height;
    private lines;
    private entryPrompt;
    private entryBuffer;
    private refresh;
    private notifyInput;
    constructor(cfg: DisplayManagerConfig);
    write(msg: string): void;
    clear(): void;
    sendKey(keyEvent: KeyboardEvent): void;
}
export interface PlayGameConfig extends DisplayManagerConfig {
    game: GameDef;
}
export declare function playGame(cfg: PlayGameConfig): void;
